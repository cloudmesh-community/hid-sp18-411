from eve import Eve
import platform

app=Eve()
@app.route('/details')
def details():
    det=[]
    det.append("Processor:\t"+platform.processor())
    det.append(" Architecture:\t"+platform.architecture().__getitem__(0))
    det.append("Platform:\t" + platform.system())
    det.append("Name:\t"+platform.machine())
    return "<br />".join(det)

if __name__=='__main__':
    app.run()