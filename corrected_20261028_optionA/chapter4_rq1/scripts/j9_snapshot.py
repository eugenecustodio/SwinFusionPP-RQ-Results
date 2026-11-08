import sys,json
sys.path.insert(0,sys.argv[1])
import ch4_content as c
rows,note=c._read_table('RQ2X/J9')
out,n=c._slim_j9(rows,note)
json.dump({'rows':out,'note':n},open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
print(len(out))
