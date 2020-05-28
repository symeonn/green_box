import numpy
import seeed_sgp30
from grove.i2c import Bus
import time

def getData():

        sgp30 = seeed_sgp30.grove_sgp30(Bus())

        co2_eq_ppm = 400
        tvoc_ppb = 0

        sample_no = 0
        sample_array = numpy.zeros((10,2))

        for lp in range(40):
                data = sgp30.read_measurements()
                co2_eq_ppm, tvoc_ppb = data.data
                #print("\r {}: tVOC = {} ppb CO2eq = {}  ".format(lp, tvoc_ppb, co2_eq_ppm))

                if co2_eq_ppm > 400 or tvoc_ppb > 0 :
                        sample_array[sample_no] = (tvoc_ppb, co2_eq_ppm)
                        sample_no +=1
                        #print(sample_array)

                if sample_no == 10 :
                        #print(sample_array)
			result = numpy.mean(sample_array, axis=0)
                        #print(result)
                        return result[0], result[1] #VOC, CO2
                        #break

                time.sleep(1)

	return getData()


#getData()
