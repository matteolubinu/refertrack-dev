#!/usr/bin/env python3
"""Cornici per i mockup dei siti (Quillino, Refertrack, sito personale).

  frame.py ios SCREENSHOT OUT.webp      stessa cornice dei post Instagram (DeviceKit, isola dinamica, tasti)
  frame.py android SCREENSHOT OUT.webp  telefono Android disegnato qui, in stile Pixel (foro della fotocamera, tasti a destra)

ios: lo screenshot viene portato a 1320 x 2868 (schermo dell'iPhone 17 Pro); le risorse della cornice stanno in
~/quillino-ios/Social/assets/bezel (variabile IOS_BEZEL per cambiarle).
Uscita: WebP con trasparenza, 1000 px di larghezza."""
import os, sys
from PIL import Image, ImageDraw

BEZEL = os.environ.get('IOS_BEZEL', os.path.expanduser('~/quillino-ios/Social/assets/bezel'))
OUT_W = 1000


def save(img, out):
    img = img.resize((OUT_W, round(OUT_W * img.height / img.width)), Image.LANCZOS)
    img.save(out, 'WEBP', quality=88, alpha_quality=100, method=6)


def ios(shot, out):
    S = 3  # 1 pt = 3 px
    B = lambda n: Image.open(os.path.join(BEZEL, n)).convert('RGBA')
    frame, mask = B('hi_PhoneComposite.png'), B('mask.png')
    mute, vol, power = B('hi_Mute_BTN.png'), B('hi_Vol_BTN.png'), B('hi_X_Power_BTN.png')
    k, w, h = 4, 126 * S, 37 * S
    pill = Image.new('L', (w * k, h * k), 0)
    ImageDraw.Draw(pill).rounded_rectangle((0, 0, w * k - 1, h * k - 1), radius=h * k // 2, fill=255)
    island = Image.new('RGBA', (w, h), (0, 0, 0, 255))
    island.putalpha(pill.resize((w, h), Image.LANCZOS))
    ox = oy = 17 * S
    canvas = Image.new('RGBA', frame.size, (0, 0, 0, 0))
    canvas.alpha_composite(mute, (8 * S, 180 * S))
    canvas.alpha_composite(vol, (8 * S, 268 * S))
    canvas.alpha_composite(vol, (8 * S, 354 * S))
    canvas.alpha_composite(power, ((474 - 8 - 16) * S, 293 * S))
    canvas.alpha_composite(frame)
    scr = Image.open(shot).convert('RGBA').resize((1320, 2868), Image.LANCZOS)
    scr.putalpha(mask.split()[3] if mask.getchannel('A').getextrema()[0] < 255 else Image.new('L', scr.size, 255))
    canvas.alpha_composite(scr, (ox, oy))
    canvas.alpha_composite(island, (ox + (440 - 126) * S // 2, oy + 11 * S))
    save(canvas, out)


def android(shot, out):
    scr = Image.open(shot).convert('RGBA')
    sw, sh = scr.size
    b = round(sw * 0.032)                 # spessore della cornice
    W, H = sw + 2 * b, sh + 2 * b
    k, btn = 3, round(sw * 0.008)         # sovracampionamento per i bordi lisci, sporgenza dei tasti
    big = lambda: Image.new('L', ((W + btn) * k, H * k), 0)

    def rr(box, r, fill=255):
        m = big()
        ImageDraw.Draw(m).rounded_rectangle([v * k for v in box], radius=r * k, fill=fill)
        return m.resize((W + btn, H), Image.LANCZOS)

    canvas = Image.new('RGBA', (W + btn, H), (0, 0, 0, 0))
    # tasti (a destra): volume e accensione
    for y0, y1 in ((H * .17, H * .25), (H * .29, H * .335)):
        m = rr((W - 3, y0, W + btn, y1), 5)
        canvas.paste(Image.new('RGBA', m.size, (46, 47, 51, 255)), (0, 0), m)
    # corpo con filo chiaro, così non sparisce sugli sfondi scuri
    outer, body = rr((0, 0, W, H), round(sw * .125)), rr((2.5, 2.5, W - 2.5, H - 2.5), round(sw * .125) - 2)
    canvas.paste(Image.new('RGBA', outer.size, (74, 76, 82, 255)), (0, 0), outer)
    canvas.paste(Image.new('RGBA', body.size, (22, 23, 26, 255)), (0, 0), body)
    # schermo
    m = rr((b, b, W - b, H - b), round(sw * .088))
    layer = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
    layer.paste(scr, (b, b))
    canvas.paste(layer, (0, 0), m)
    # foro della fotocamera
    r = round(sw * .021)
    cx, cy = W // 2, b + round(sw * .052)
    hole = rr((cx - r, cy - r, cx + r, cy + r), r)
    canvas.paste(Image.new('RGBA', hole.size, (6, 6, 8, 255)), (0, 0), hole)
    save(canvas, out)


if __name__ == '__main__':
    if len(sys.argv) != 4 or sys.argv[1] not in ('ios', 'android'):
        sys.exit(__doc__)
    {'ios': ios, 'android': android}[sys.argv[1]](sys.argv[2], sys.argv[3])
