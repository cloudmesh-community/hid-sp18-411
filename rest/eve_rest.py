from eve import Eve
import platform
import json

settings = {'MONGO_HOST': 'localhost', 'MONGO_PORT': 27017, 'DOMAIN': {}}

app = Eve()


@app.route('/details')
def details(settings=settings):
    det = []
    det.append("Processor:" + platform.processor())
    det.append(" Architecture:" + platform.architecture().__getitem__(0))
    det.append("Platform:" + platform.system())
    det.append("Name:" + platform.machine())
    return json.dumps(det)


if __name__ == '__main__':
    app.run()
