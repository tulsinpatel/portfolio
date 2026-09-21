import os, random
OUT = "/Users/tulsipatel/Desktop/tulsiportfoliosite/images"

INK="#43262E"; PAPER="#FFFCFB"; CORAL="#084C61"; INDIGO="#96C5F7"; SAGE="#9EBC9F"; LILAC="#FAB3A9"; BUTTER="#96C5F7"

def wrap(w,h,body,bg):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Product screenshot placeholder">
<defs>
<linearGradient id="g1" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="{bg}"/><stop offset="1" stop-color="{bg}" stop-opacity="0.72"/>
</linearGradient>
<filter id="soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="26"/></filter>
</defs>
<rect width="{w}" height="{h}" fill="url(#g1)"/>
{body}
</svg>'''

def browser(w,h,bg,accent,title,kind):
    b=[]
    b.append(f'<circle cx="{w*0.82:.0f}" cy="{h*0.18:.0f}" r="{h*0.34:.0f}" fill="{accent}" opacity="0.30" filter="url(#soft)"/>')
    b.append(f'<circle cx="{w*0.12:.0f}" cy="{h*0.88:.0f}" r="{h*0.28:.0f}" fill="{PAPER}" opacity="0.22" filter="url(#soft)"/>')
    # window
    x,y,ww,hh = w*0.09, h*0.14, w*0.82, h*0.74
    b.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{ww:.0f}" height="{hh:.0f}" rx="16" fill="{PAPER}" opacity="0.97"/>')
    b.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{ww:.0f}" height="34" rx="16" fill="{INK}" opacity="0.07"/>')
    b.append(f'<rect x="{x:.0f}" y="{y+22:.0f}" width="{ww:.0f}" height="12" fill="{PAPER}" opacity="0.97"/>')
    for i,c in enumerate([CORAL,BUTTER,SAGE]):
        b.append(f'<circle cx="{x+20+i*16:.0f}" cy="{y+17:.0f}" r="4.5" fill="{c}"/>')
    b.append(f'<rect x="{x+72:.0f}" y="{y+10:.0f}" width="{ww*0.45:.0f}" height="14" rx="7" fill="{INK}" opacity="0.10"/>')
    ix,iy,iw,ih = x+22, y+50, ww-44, hh-72
    if kind=="dashboard":
        b.append(f'<rect x="{ix:.0f}" y="{iy:.0f}" width="{iw*0.22:.0f}" height="{ih:.0f}" rx="10" fill="{INK}" opacity="0.055"/>')
        for i in range(5):
            b.append(f'<rect x="{ix+14:.0f}" y="{iy+18+i*26:.0f}" width="{iw*0.22-40:.0f}" height="8" rx="4" fill="{INK}" opacity="{0.22 if i==1 else 0.10}"/>')
        cx = ix+iw*0.26
        cw = iw*0.74
        for i in range(3):
            b.append(f'<rect x="{cx+i*(cw/3):.0f}" y="{iy:.0f}" width="{cw/3-12:.0f}" height="{ih*0.26:.0f}" rx="10" fill="{accent}" opacity="{0.16+i*0.09:.2f}"/>')
            b.append(f'<rect x="{cx+i*(cw/3)+14:.0f}" y="{iy+18:.0f}" width="34" height="8" rx="4" fill="{INK}" opacity="0.28"/>')
            b.append(f'<rect x="{cx+i*(cw/3)+14:.0f}" y="{iy+36:.0f}" width="62" height="16" rx="6" fill="{INK}" opacity="0.5"/>')
        gy = iy+ih*0.32
        gh = ih*0.68
        b.append(f'<rect x="{cx:.0f}" y="{gy:.0f}" width="{cw-12:.0f}" height="{gh:.0f}" rx="12" fill="{INK}" opacity="0.045"/>')
        random.seed(7)
        pts=[]
        n=14
        for i in range(n):
            px = cx+20 + i*((cw-52)/(n-1))
            py = gy+gh-24 - (0.18+0.62*((i/n)**0.85)+random.uniform(-0.09,0.09))*(gh-52)
            pts.append((px,py))
        d = "M " + " L ".join(f"{p[0]:.0f} {p[1]:.0f}" for p in pts)
        area = d + f" L {pts[-1][0]:.0f} {gy+gh-24:.0f} L {pts[0][0]:.0f} {gy+gh-24:.0f} Z"
        b.append(f'<path d="{area}" fill="{accent}" opacity="0.16"/>')
        b.append(f'<path d="{d}" fill="none" stroke="{accent}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
        for p in pts[::4]:
            b.append(f'<circle cx="{p[0]:.0f}" cy="{p[1]:.0f}" r="4.5" fill="{PAPER}" stroke="{accent}" stroke-width="3"/>')
    elif kind=="table":
        b.append(f'<rect x="{ix:.0f}" y="{iy:.0f}" width="{iw*0.4:.0f}" height="18" rx="9" fill="{INK}" opacity="0.30"/>')
        b.append(f'<rect x="{ix+iw-120:.0f}" y="{iy-2:.0f}" width="120" height="30" rx="15" fill="{accent}" opacity="0.9"/>')
        ry = iy+44
        for i in range(6):
            op = 0.05 if i%2 else 0.085
            b.append(f'<rect x="{ix:.0f}" y="{ry+i*((ih-56)/6):.0f}" width="{iw:.0f}" height="{(ih-56)/6-8:.0f}" rx="8" fill="{INK}" opacity="{op}"/>')
            yy = ry+i*((ih-56)/6)+((ih-56)/6-8)/2-4
            b.append(f'<circle cx="{ix+20:.0f}" cy="{yy+4:.0f}" r="8" fill="{[CORAL,INDIGO,SAGE,BUTTER,LILAC,CORAL][i]}" opacity="0.75"/>')
            b.append(f'<rect x="{ix+40:.0f}" y="{yy:.0f}" width="{iw*0.3:.0f}" height="9" rx="4" fill="{INK}" opacity="0.22"/>')
            b.append(f'<rect x="{ix+iw*0.42:.0f}" y="{yy:.0f}" width="{iw*0.16:.0f}" height="9" rx="4" fill="{INK}" opacity="0.13"/>')
            b.append(f'<rect x="{ix+iw*0.64:.0f}" y="{yy-3:.0f}" width="{iw*0.13:.0f}" height="16" rx="8" fill="{accent}" opacity="0.22"/>')
    elif kind=="editor":
        b.append(f'<rect x="{ix:.0f}" y="{iy:.0f}" width="{iw*0.58:.0f}" height="{ih:.0f}" rx="10" fill="{INK}" opacity="0.05"/>')
        random.seed(3)
        for i in range(9):
            wd = random.uniform(0.2,0.86)*(iw*0.58-40)
            b.append(f'<rect x="{ix+20:.0f}" y="{iy+22+i*((ih-44)/9):.0f}" width="{wd:.0f}" height="9" rx="4" fill="{INK}" opacity="{0.20 if i in (0,4) else 0.10}"/>')
        px = ix+iw*0.62
        pw = iw*0.38
        b.append(f'<rect x="{px:.0f}" y="{iy:.0f}" width="{pw:.0f}" height="{ih*0.5:.0f}" rx="10" fill="{accent}" opacity="0.18"/>')
        b.append(f'<circle cx="{px+pw/2:.0f}" cy="{iy+ih*0.25:.0f}" r="{ih*0.14:.0f}" fill="{accent}" opacity="0.45"/>')
        b.append(f'<rect x="{px:.0f}" y="{iy+ih*0.56:.0f}" width="{pw:.0f}" height="{ih*0.44:.0f}" rx="10" fill="{INK}" opacity="0.05"/>')
        for i in range(3):
            b.append(f'<rect x="{px+16:.0f}" y="{iy+ih*0.56+20+i*26:.0f}" width="{pw-32-i*18:.0f}" height="9" rx="4" fill="{INK}" opacity="0.13"/>')
    return wrap(w,h,"\n".join(b),bg)

def mobile(w,h,bg,accent):
    b=[]
    b.append(f'<circle cx="{w*0.2:.0f}" cy="{h*0.2:.0f}" r="{h*0.3:.0f}" fill="{accent}" opacity="0.30" filter="url(#soft)"/>')
    pw,ph = w*0.34, h*0.82
    x,y = (w-pw)/2, (h-ph)/2
    b.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{pw:.0f}" height="{ph:.0f}" rx="34" fill="{INK}" opacity="0.9"/>')
    b.append(f'<rect x="{x+7:.0f}" y="{y+7:.0f}" width="{pw-14:.0f}" height="{ph-14:.0f}" rx="28" fill="{PAPER}"/>')
    b.append(f'<rect x="{x+pw/2-26:.0f}" y="{y+16:.0f}" width="52" height="10" rx="5" fill="{INK}" opacity="0.85"/>')
    ix,iy,iw = x+22, y+50, pw-44
    b.append(f'<rect x="{ix:.0f}" y="{iy:.0f}" width="{iw*0.55:.0f}" height="14" rx="7" fill="{INK}" opacity="0.3"/>')
    b.append(f'<rect x="{ix:.0f}" y="{iy+30:.0f}" width="{iw:.0f}" height="{ph*0.26:.0f}" rx="14" fill="{accent}" opacity="0.25"/>')
    b.append(f'<circle cx="{ix+iw/2:.0f}" cy="{iy+30+ph*0.13:.0f}" r="{ph*0.075:.0f}" fill="{accent}" opacity="0.55"/>')
    for i in range(3):
        yy = iy+40+ph*0.26+i*(ph*0.115)
        b.append(f'<rect x="{ix:.0f}" y="{yy:.0f}" width="{iw:.0f}" height="{ph*0.09:.0f}" rx="12" fill="{INK}" opacity="0.06"/>')
        b.append(f'<circle cx="{ix+22:.0f}" cy="{yy+ph*0.045:.0f}" r="10" fill="{[CORAL,INDIGO,SAGE][i]}" opacity="0.7"/>')
        b.append(f'<rect x="{ix+42:.0f}" y="{yy+ph*0.045-9:.0f}" width="{iw*0.45:.0f}" height="8" rx="4" fill="{INK}" opacity="0.2"/>')
        b.append(f'<rect x="{ix+42:.0f}" y="{yy+ph*0.045+3:.0f}" width="{iw*0.3:.0f}" height="7" rx="3.5" fill="{INK}" opacity="0.11"/>')
    b.append(f'<rect x="{x+7:.0f}" y="{y+ph-64:.0f}" width="{pw-14:.0f}" height="57" fill="{INK}" opacity="0.045"/>')
    for i in range(4):
        b.append(f'<circle cx="{x+30+i*((pw-60)/3):.0f}" cy="{y+ph-36:.0f}" r="7" fill="{accent if i==0 else INK}" opacity="{0.9 if i==0 else 0.18}"/>')
    return wrap(w,h,"\n".join(b),bg)

def portrait(w,h):
    b=[]
    b.append(f'<circle cx="{w*0.5:.0f}" cy="{h*0.34:.0f}" r="{w*0.5:.0f}" fill="{CORAL}" opacity="0.35" filter="url(#soft)"/>')
    b.append(f'<circle cx="{w*0.5:.0f}" cy="{h*0.33:.0f}" r="{w*0.21:.0f}" fill="{PAPER}" opacity="0.92"/>')
    b.append(f'<path d="M {w*0.14:.0f} {h*1.02:.0f} a {w*0.36:.0f} {h*0.42:.0f} 0 0 1 {w*0.72:.0f} 0 Z" fill="{PAPER}" opacity="0.92"/>')
    b.append(f'<text x="{w*0.5:.0f}" y="{h*0.93:.0f}" text-anchor="middle" font-family="Georgia,serif" font-size="{w*0.055:.0f}" fill="{INK}" opacity="0.45">your photo here</text>')
    return wrap(w,h,"\n".join(b),"#E4F0FD")

# canvas colour, then the accent drawn on top of it
files = {
 "project-01.svg": browser(1200,800,"#96C5F7","#084C61","",'dashboard'),
 "project-02.svg": mobile(1200,800,"#FAB3A9","#084C61"),
 "project-03.svg": browser(1200,800,"#9EBC9F","#084C61","",'table'),
 "project-04.svg": browser(1200,800,"#EAF2E9","#084C61","",'editor'),
 "project-05.svg": mobile(1200,800,"#FDEAE6","#084C61"),
 "project-06.svg": browser(1200,800,"#E4F0FD","#084C61","",'dashboard'),
 "project-07.svg": browser(1200,800,"#FDEAE6","#084C61","",'table'),
 "project-08.svg": mobile(1200,800,"#EAF2E9","#084C61"),
 "portrait.svg": portrait(900,1100),
}
for k,v in files.items():
    open(os.path.join(OUT,k),"w").write(v)
print("\n".join(sorted(files)))
