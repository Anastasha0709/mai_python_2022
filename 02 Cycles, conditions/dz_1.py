drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro", "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus", "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3", "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

#в drone по очереди попадает каждый дрон из списка drone_list
for drone in drone_list:
	print(drone)

#TODO1
#выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество. 
#учтите, что:
#1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
#2) при выводе исправьте название производителя, если допущена ошибка. правильный вариант названия: DJI, Autel

p_n = input("Введите название производителя: ")
sp_drons=[]
for drone in drone_list:
	if p_n.lower() in drone.lower() :
		dsp_drons.append(drone)
print(f"Модели дронов этого производителя :/n {sp_drons}./n Общее количество моделей {len(sp_drons)}")





#TODO2
#подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine

DJI_kol=[]
Autel_kol=[]
Parrot_kol=[]
Ryze_kol = []
Eachine_kol=[]
for drone in drone_list:
	if "DJI" in drone:
		DJI_kol.append(drone)
	elif "Autel" in drone:
		Autel_kol.append(drone)
	elif "Parrot" in drone:
		Parrot_kol.append(drone)
	elif "Ryze" in drone:
		Ryze_kol.append(drone)
	else:
		Eachine_kol.append(drone)
print(len(DJI_kol))
print(len(Autel_kol))
print(len(Parrot_kol))
print(len(Ryze_kol))
print(len(Eachine_kol))


#TODO3
#выведите все дроны из списка, которые нужно регистрировать (масса больше 150 г), и подсчитайте их количество. 
#сделайте то же самое для всех дронов, которые не нужно регистрировать
#для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
#как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь
bigger = []
smaller=[]
for drone, weight in zip(drone_list,  drone_weight_list):
	if weight > 150:
		bigger.append(drone)
	else:
		smaller.append(drone)
print(len(bigger))
print(len(smaller))



	

#TODO4
#для каждого дрона из списка выведите, нужно ли согласовывать полет при следующих условиях:
#высота 100 м, полет над населенным пунктом, вне закрытых зон, в прямой видимости
#помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!
while True:
	y_p = input("Введите условия полета, чтобы закончить введите q")
	n_d = input("Введите название дрона")
	if y_p == 'q' :
		break
	else:
		for drone,weight in zip(drone_list, drone_weight_list):
			if n_d in drone and weight> 150 and y_p == "полет над населенным пунктом":
				print("Нужно согласовать полет!")
			elif n_d in drone :
				print("Не нужно согласовать полет!")
		    else:
		    	pass

#TODO5*
#модифицируйте решение задания TODO1:
#теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
#например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
#производители те же: DJI, Autel, Parrot, Ryze, Eachine

