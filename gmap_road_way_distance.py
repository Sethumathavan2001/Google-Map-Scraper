import requests,json,pandas,time

df = pandas.read_csv(r"D:\Sethu\Gayu\1_Outlet_Coverage_StateHighway\new\Highway_Outlets_Sethu.csv")

def gmapdist(out,subd):
    print('Gmap')
    url = f'https://www.google.com/maps/preview/directions?authuser=0&hl=en&gl=in&pb=!1m4!3m2!3d{subd[0]}!4d{subd[1]}!6e2!1m5!1s{out[0]}%2C{out[1]}!3m2!3d{out[0]}!4d{out[1]}!6e2!3m12!1m3!1d25204.40651808625!2d{(subd[1]+out[1])/2}!3d{(subd[0]+out[0])/2}!2m3!1f0!2f0!3f0!3m2!1i1366!2i170!4f13.1!6m35!1m1!18b1!2m3!5m1!6e2!20e3!6m14!4b1!49b1!74i150000!75b1!85b1!89b1!91b1!101i97!114b1!149b1!171b1!176f8!179f90!182b1!10b1!12b1!13b1!14b1!16b1!17m1!3e1!20m6!1e0!2e3!5e2!6b1!8b1!14b1!8m0!15m4!1sjpKCZeXXDbbk4-EPq5KkkAo!4m1!2i17307!7e81!20m0!27b1!28m0!40i675!47m0'
    n=1
    while n<4:
        try:
            pg=requests.get(url)
            data = json.loads(pg.text[5:])
            distance = data[0][1][0][0][2][0]/1000
            time = data[0][1][0][0][3][0]/60
            return (distance,time)
        except:
            print('Sleeping..')
            time.sleep(n*10)
            n+=1
# df['Gmap_Distance'] = df.apply(lambda x:gmapdist(x),axis=1)