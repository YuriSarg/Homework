import argparse
import xlsxwriter

#Функции для консолньой команды

def cons_argum():
   parser = argparse.ArgumentParser()
   parser.add_argument('-f', '--file', required=True, help = 'File.txt')
   parser.add_argument('-x', '--xlsx', default="Profbook", help = 'File.exel')
   args = parser.parse_args()
   return args.file, args.xlsx

#Функция cont(data_file) принимает в качестве аргумента имя текстового файла data_file. 
#Функция читает этот файл и возвращает отсортированный список строк.

def cont(data_file):
   with open(data_file) as f:
       lis = []
       for el in f:
           lis.append(el.split())
       sort_lis = sorted(lis, reverse=True, key=lambda x : x[2])
       for x in sort_lis:
           x[2] = int(x[2])
       return sort_lis

#Функция proffbook(wbname) создает новый файл Excel, открывает его для записи и добавляет новый лист с именем "Sheet1"

def proffbook(wbname):
   workbook = xlsxwriter.Workbook(wbname)
   worksheet = workbook.add_worksheet()
   worksheet.set_column(0, 3, 10)
   form = workbook.add_format(({'bold': True, 'bg_color': '#FFFF00'}))
   worksheet.write('A1', 'Name', form)
   worksheet.write('B1', 'Surname', form)
   worksheet.write('C1', 'Age', form)
   worksheet.write('D1', 'Profession', form)
   return workbook, worksheet

#Эта функция заполняет таблицу Excel данными из переданного списка cont. Она также применяет форматирование к ячейкам столбца 
#"Возраст" - если значение возраста меньше 21 то цвет будет красным

def fill_data(workbook, worksheet, cont):
   form1 = workbook.add_format(({'bold': False, 'bg_color': '#ff0019'}))
   for i, (name, surname, age, profession) in enumerate(cont, start=2):
       worksheet.conditional_format(f'C{i}', {'type': 'cell', 'criteria': '<', 'value': 21, 'format': form1})
       worksheet.write(f'A{i}', name)
       worksheet.write(f'B{i}', surname)
       worksheet.write(f'C{i}', age, )
       worksheet.write(f'D{i}', profession)
   workbook.close()

def main():
   filename, xlsxname = cons_argum()
   mylis = cont(filename)
   prof_b, prof_sh = proffbook(xlsxname)
   fill_data(prof_b, prof_sh, mylis)

main()
