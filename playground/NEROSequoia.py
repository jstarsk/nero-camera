import ptpy


class NEROSequoia:

    @staticmethod
    def triggerCamera():

        camera = ptpy.PTPy()
        with camera.session():
            capture = camera.initiate_capture()
            print (capture)
            evt = camera.event()
            if evt:
                print(evt)
            print ("-------")
