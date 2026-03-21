from PIL import Image , ImageEnhance

im= Image.open("Little power robot.gif")

frames =[]

for frme in range (im.n_frames):
   im.seek(frme)
   frameimage =im.convert("RGBA")

   data  = frameimage.getdata()
   newdata=[]
   for item in data:
      if item[0] < 50 and item[1] <50 and item[2] < 50 :
         newdata.append((255,105,180 ,item[3]))
      else:
         newdata.append(item)
   frameimage.putdata(newdata)
   frames.append(frameimage)

frames[0].save("Little power robot .gif" , save_all=True , append_image=frames[1:] , loop=0 , duration=im.info['duration'])
