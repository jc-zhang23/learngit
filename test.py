from PyCAVSim import PyCAVSim
from PyCAVSim.inloop import ReplayClan
from PyCAVSim.map.main import MTSMap
from PyCAVSim.outloop.gui import CAVGUI
from PyCAVSim.utils.log import set_default_logger
import logging

logger = set_default_logger(level = logging.INFO)



# 仿真设定
# 基础项
map_data = MTSMap.from_mtsdb("./examples/following_test/ZS.mtsdb.map")
# 环内流程项
family = ReplayClan("./examples/following_test/ZS-0.mtsdb")
# 环外流程项
gui = CAVGUI()



pycav = PyCAVSim(
    map = map_data, 
    ips = [family], 
    ops = {"gui": gui}, 
    max_step = family.iteror.max_step, 
)

if __name__ == "__main__": 
    pycav.run()