# class Swift:
#     def start(self):
#         print("swift car start")
#     def accelerate(self):           #self is not mandatory
#         print("swift car accelerating functionality")
#     def breaks(self):
#         print("swift car break method")
#     def stop(self):
#         print("swift car stopping")
# class Seltos:
#     def start(self):
#         print("seltos car start")
#     def accelerate(self):           #self is not mandatory
#         print("seltos car accelerating functionality")
#     def breaks(self):
#         print("seltos car break method")
#     def stop(self):
#         print("seltos car stopping")
# class Person:
#     def drive(self,car):
#         car.start()
#         car.accelerate()
#         car.breaks()
#         car.stop()
# p=Person()
# sw=Swift()
# p.drive(sw)
#
#
class Pycharm:
    def compile(self):
        print("compile using pycharm")
    def execute(self):
        print("execute")
class Vscode:
    def compile(self):
        print("compile using vscode")
    def execute(self):
        print("vscode execute")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
p=Programmer()
pyc=Vscode()
p.coding(pyc)
