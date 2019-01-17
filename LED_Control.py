import pigpio
import time

pi1 = pigpio.pi()

try:
        while True:
		# Red LED
                for dc in range(0, 101, 5):   # Increase duty cycle: 0~100
                        pi1.set_PWM_dutycycle(19, dc)     # Change duty cycle
			time.sleep(0.05)
                time.sleep(0.5)
                for dc in range(100, -1, -5): # Decrease duty cycle: 100~0
                        pi1.set_PWM_dutycycle(19, dc)
                        time.sleep(0.05)
                time.sleep(0.5)

		# Green LED
                for dc in range(0, 101, 5):   # Increase duty cycle: 0~100
                        pi1.set_PWM_dutycycle(26, dc)     # Change duty cycle
                        time.sleep(0.05)
                time.sleep(0.5)
                for dc in range(100, -1, -5): # Decrease duty cycle: 100~0
                        pi1.set_PWM_dutycycle(26, dc)
                        time.sleep(0.05)
                time.sleep(0.5)

		# Blue LED
                for dc in range(0, 101, 5):   # Increase duty cycle: 0~100
                        pi1.set_PWM_dutycycle(13, dc)     # Change duty cycle
                        time.sleep(0.05)
                time.sleep(0.5)
                for dc in range(100, -1, -5): # Decrease duty cycle: 100~0
                        pi1.set_PWM_dutycycle(13, dc)
                        time.sleep(0.05)
                time.sleep(0.5)

		# White LED
                for dc in range(0, 101, 5):   # Increase duty cycle: 0~100
                        pi1.set_PWM_dutycycle(13, dc)
			pi1.set_PWM_dutycycle(26, dc)
			pi1.set_PWM_dutycycle(19, dc)
                        time.sleep(0.05)
                time.sleep(0.5)
                for dc in range(100, -1, -5): # Decrease duty cycle: 100~0
                        pi1.set_PWM_dutycycle(13, dc)
			pi1.set_PWM_dutycycle(26, dc)
			pi1.set_PWM_dutycycle(19, dc)
                        time.sleep(0.05)
                time.sleep(0.5)


except KeyboardInterrupt:
        pi1.stop()
