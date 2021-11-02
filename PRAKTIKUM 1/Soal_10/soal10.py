print(1194006 % 8)
import shapefile
w=shapefile.Writer("soal10", shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("tomo","satu")

w.poly([[[-5, 5], [5, 5], [10, -5], [-5, -5], [-5, 5]]])

w.close()