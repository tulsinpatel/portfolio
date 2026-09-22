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
    elif kind=="code":
        code_w = iw*0.68
        b.append(f'<rect x="{ix:.0f}" y="{iy:.0f}" width="{code_w:.0f}" height="{ih:.0f}" rx="10" fill="{INK}" opacity="0.92"/>')
        b.append(f'<rect x="{ix:.0f}" y="{iy:.0f}" width="{code_w:.0f}" height="34" rx="10" fill="{PAPER}" opacity="0.08"/>')
        for i in range(3):
            b.append(f'<rect x="{ix+18+i*78:.0f}" y="{iy+12:.0f}" width="58" height="9" rx="4" fill="{PAPER}" opacity="{0.34 if i==0 else 0.12}"/>')
        syntax = ["#96C5F7", "#FAB3A9", "#9EBC9F", "#FFFCFB"]
        for i in range(11):
            yy = iy+52+i*((ih-70)/11)
            b.append(f'<text x="{ix+17:.0f}" y="{yy+8:.0f}" font-family="monospace" font-size="10" fill="{PAPER}" opacity="0.25">{i+1:02}</text>')
            indent = (i%4)*13
            x0 = ix+46+indent
            for j in range(1+(i%3)):
                wd = 48 + ((i*23+j*31)%92)
                b.append(f'<rect x="{x0:.0f}" y="{yy:.0f}" width="{wd:.0f}" height="9" rx="4" fill="{syntax[(i+j)%len(syntax)]}" opacity="{0.72-j*0.12:.2f}"/>')
                x0 += wd+9
        px = ix+code_w+14
        pw = iw-code_w-14
        b.append(f'<rect x="{px:.0f}" y="{iy:.0f}" width="{pw:.0f}" height="{ih*0.62:.0f}" rx="10" fill="{accent}" opacity="0.17"/>')
        b.append(f'<circle cx="{px+pw/2:.0f}" cy="{iy+ih*0.31:.0f}" r="{ih*0.13:.0f}" fill="{accent}" opacity="0.48"/>')
        b.append(f'<rect x="{px:.0f}" y="{iy+ih*0.67:.0f}" width="{pw:.0f}" height="{ih*0.33:.0f}" rx="10" fill="{INK}" opacity="0.06"/>')
        for i in range(3):
            b.append(f'<rect x="{px+16:.0f}" y="{iy+ih*0.67+18+i*23:.0f}" width="{pw-32-i*19:.0f}" height="8" rx="4" fill="{INK}" opacity="0.14"/>')
    elif kind=="flow":
        b.append(f'<rect x="{ix:.0f}" y="{iy:.0f}" width="{iw:.0f}" height="34" rx="10" fill="{INK}" opacity="0.055"/>')
        for i in range(4):
            b.append(f'<rect x="{ix+16+i*44:.0f}" y="{iy+12:.0f}" width="28" height="9" rx="4" fill="{INK}" opacity="{0.22 if i==0 else 0.10}"/>')
        nodes = [
            (ix+48, iy+ih*0.32, 150, 74),
            (ix+iw*0.40, iy+ih*0.16, 176, 82),
            (ix+iw*0.40, iy+ih*0.58, 176, 82),
            (ix+iw-218, iy+ih*0.36, 170, 82),
        ]
        def center(n): return (n[0]+n[2]/2, n[1]+n[3]/2)
        for a,c in [(0,1),(0,2),(1,3),(2,3)]:
            ax,ay=center(nodes[a]); cx,cy=center(nodes[c]); mid=(ax+cx)/2
            b.append(f'<path d="M {ax:.0f} {ay:.0f} C {mid:.0f} {ay:.0f}, {mid:.0f} {cy:.0f}, {cx:.0f} {cy:.0f}" fill="none" stroke="{accent}" stroke-width="4" opacity="0.48"/>')
        colors=[CORAL,INDIGO,SAGE,LILAC]
        for i,(nx,ny,nw,nh) in enumerate(nodes):
            b.append(f'<rect x="{nx:.0f}" y="{ny:.0f}" width="{nw:.0f}" height="{nh:.0f}" rx="13" fill="{PAPER}" stroke="{colors[i]}" stroke-width="3"/>')
            b.append(f'<circle cx="{nx+22:.0f}" cy="{ny+nh/2:.0f}" r="10" fill="{colors[i]}" opacity="0.75"/>')
            b.append(f'<rect x="{nx+42:.0f}" y="{ny+nh/2-13:.0f}" width="{nw-62:.0f}" height="10" rx="5" fill="{INK}" opacity="0.25"/>')
            b.append(f'<rect x="{nx+42:.0f}" y="{ny+nh/2+7:.0f}" width="{(nw-62)*0.67:.0f}" height="8" rx="4" fill="{INK}" opacity="0.10"/>')
    elif kind=="cards":
        b.append(f'<rect x="{ix:.0f}" y="{iy:.0f}" width="{iw*0.42:.0f}" height="18" rx="9" fill="{INK}" opacity="0.28"/>')
        b.append(f'<rect x="{ix:.0f}" y="{iy+29:.0f}" width="{iw*0.62:.0f}" height="9" rx="4" fill="{INK}" opacity="0.10"/>')
        gap=14; card_w=(iw-gap)/2; card_h=(ih-68-gap)/2
        colors=[INDIGO,SAGE,LILAC,CORAL]
        for i in range(4):
            cx=ix+(i%2)*(card_w+gap); cy=iy+58+(i//2)*(card_h+gap)
            b.append(f'<rect x="{cx:.0f}" y="{cy:.0f}" width="{card_w:.0f}" height="{card_h:.0f}" rx="13" fill="{INK}" opacity="0.045" stroke="{INK}" stroke-opacity="0.08"/>')
            b.append(f'<rect x="{cx+18:.0f}" y="{cy+18:.0f}" width="42" height="42" rx="11" fill="{colors[i]}" opacity="0.58"/>')
            b.append(f'<rect x="{cx+76:.0f}" y="{cy+21:.0f}" width="{card_w-98:.0f}" height="11" rx="5" fill="{INK}" opacity="0.28"/>')
            b.append(f'<rect x="{cx+76:.0f}" y="{cy+42:.0f}" width="{(card_w-98)*0.7:.0f}" height="8" rx="4" fill="{INK}" opacity="0.11"/>')
            for j in range(2):
                b.append(f'<rect x="{cx+18:.0f}" y="{cy+78+j*22:.0f}" width="{card_w-36-j*34:.0f}" height="8" rx="4" fill="{INK}" opacity="0.09"/>')
    elif kind=="feed":
        b.append(f'<rect x="{ix:.0f}" y="{iy:.0f}" width="{iw:.0f}" height="28" rx="9" fill="{INK}" opacity="0.055"/>')
        for i in range(5):
            b.append(f'<rect x="{ix+18+i*76:.0f}" y="{iy+10:.0f}" width="54" height="8" rx="4" fill="{INK}" opacity="{0.22 if i==0 else 0.09}"/>')
        fy=iy+44; left_w=iw*0.58
        b.append(f'<rect x="{ix:.0f}" y="{fy:.0f}" width="{left_w:.0f}" height="{ih-44:.0f}" rx="13" fill="{accent}" opacity="0.18"/>')
        b.append(f'<rect x="{ix+18:.0f}" y="{fy+18:.0f}" width="{left_w-36:.0f}" height="{(ih-44)*0.58:.0f}" rx="10" fill="{accent}" opacity="0.34"/>')
        b.append(f'<rect x="{ix+18:.0f}" y="{fy+(ih-44)*0.66:.0f}" width="{left_w*0.76:.0f}" height="13" rx="6" fill="{INK}" opacity="0.32"/>')
        b.append(f'<rect x="{ix+18:.0f}" y="{fy+(ih-44)*0.73:.0f}" width="{left_w*0.58:.0f}" height="10" rx="5" fill="{INK}" opacity="0.15"/>')
        rx=ix+left_w+16; rw=iw-left_w-16
        for i in range(3):
            cy=fy+i*((ih-44)/3)
            b.append(f'<rect x="{rx:.0f}" y="{cy:.0f}" width="{rw:.0f}" height="{(ih-44)/3-12:.0f}" rx="11" fill="{INK}" opacity="0.045"/>')
            b.append(f'<rect x="{rx+13:.0f}" y="{cy+13:.0f}" width="{rw*0.34:.0f}" height="{(ih-44)/3-38:.0f}" rx="8" fill="{[SAGE,LILAC,INDIGO][i]}" opacity="0.47"/>')
            b.append(f'<rect x="{rx+rw*0.41:.0f}" y="{cy+18:.0f}" width="{rw*0.49:.0f}" height="10" rx="5" fill="{INK}" opacity="0.24"/>')
            b.append(f'<rect x="{rx+rw*0.41:.0f}" y="{cy+39:.0f}" width="{rw*0.38:.0f}" height="8" rx="4" fill="{INK}" opacity="0.11"/>')
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
 "project-01.svg": browser(1200,800,"#96C5F7","#084C61","",'editor'),
 "project-02.svg": mobile(1200,800,"#FAB3A9","#084C61"),
 "project-03.svg": browser(1200,800,"#9EBC9F","#084C61","",'cards'),
 "project-04.svg": browser(1200,800,"#EAF2E9","#084C61","",'code'),
 "project-05.svg": browser(1200,800,"#FDEAE6","#084C61","",'feed'),
 "project-06.svg": browser(1200,800,"#E4F0FD","#084C61","",'flow'),
 "project-07.svg": browser(1200,800,"#FDEAE6","#084C61","",'table'),
 "project-08.svg": mobile(1200,800,"#EAF2E9","#084C61"),
 "portrait.svg": portrait(900,1100),
}
for k,v in files.items():
    open(os.path.join(OUT,k),"w").write(v)
print("\n".join(sorted(files)))
