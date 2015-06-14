from Simulator import *

app = Simulator()
app.after(20, app.simLoop)
app.mainloop()


"""
 vik wiki szabalyozastechnika gyakorlat

 atviteli fuggveny
 output / input     egy tagra

 tobb tag: -sorban -> atv fvek szorzodnak
           -parhuzamosa -> atv fvek osszeadodnak 

 szabalyzo modellje: tavolsag a celtol, ez milyen gyorsan valtozik
 szabalyzo : 2 bemenet: hova, aktualis -> hibajel       -> 1 bemenet
             1 kimenet -> vezerles
             linearis -> hibajel * konstans

 hibajel derivaltja -> gyorsitja a konvergenciat
 hibak integralja az eltelt ido alatt -> pontositja a vezerlest

  => szabalyzo:    
         hibajel =: h
         h*k1 + dh*k2 + hSum

"""