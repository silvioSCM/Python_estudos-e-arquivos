import os
import time

os.system('clear')
print('\033[36mInicaindo teste de processamento...\033[37m')
for n in range(1,5):
	os.system('ls -laR /')
	time.sleep(180)
print('\033[32mFinalizado!!!\033[37m')
sair = input('\033[32mPressione ENTER!!\033[37m')
quit()

