#!/bin/bash
# build -> apply edits -> clean copy -> render -> page numbers; repeat until the page numbers stop changing
S=$1; T=$S/ch4/team/final_check; R=$S/render; set -e
for it in 1 2 3 4; do
  cd $S/ch4/tools
  python3 build_ch4.py $S/ch4/thesis_before_ch4_backup.docx $S/ch4/final_a.docx >/dev/null
  python3 apply_edits.py $S/ch4/final_a.docx $T/edits_all.json $S/ch4/final_c.docx > $T/apply_report_all.txt
  python3 layout_fixes.py $S/ch4/final_c.docx $S/ch4/final_b.docx
  python3 accept_all.py $S/ch4/final_b.docx $R/final.docx >/dev/null
  python3 render_copy.py $R/final.docx $R/final_render.docx
  SAL_USE_VCLPLUGIN=svp timeout 900 $S/lo/root/opt/libreoffice26.2/program/soffice -env:UserInstallation=file://$S/lo_profile --headless --convert-to pdf --outdir $R $R/final_render.docx >/dev/null 2>&1
  mv $R/final_render.pdf $R/final.pdf
  python3 pagenums.py $R/final.pdf $R/final.docx $T/page_map_check.json
  [ -f $T/page_map.json ] || echo '{"toc":{},"fig":{},"tab":{},"front":{}}' > $T/page_map_none.json
  N=$(python3 -c "
import json,os
a=json.load(open('$T/page_map.json')) if os.path.exists('$T/page_map.json') else {'toc':{},'fig':{},'tab':{},'front':{}}
b=json.load(open('$T/page_map_check.json'))
print(sum(a[s].get(k)!=b[s].get(k) for s in b for k in set(a[s])|set(b[s])))")
  echo "iteration $it: page-number changes $N"
  cp $T/page_map_check.json $T/page_map.json
  [ "$N" = "0" ] && break
done
