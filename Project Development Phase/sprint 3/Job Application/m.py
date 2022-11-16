from csv import DictWriter


def home(a,b,c,d,e,f,g,h,i,j,k,l,m,n):
             field_names = ['job_ID', 'Company',
			'Role', 'Experience','Skill','Vacancy','Stream','Location','Salary','Website','Logo','date posted','last date to apply','job description link']

             dict = {'job_ID':a, 'Company':b,
			'Role':c, 'Experience':d,'Skill':e,'Vacancy':f,'Stream':g,'Location':h,'Salary':i,'Website':j,'Logo':k,'date posted':l,'last date to apply':m,'job description link':n}

             with open('data.csv', 'a',newline='') as f_object:

                  dictwriter_object = DictWriter(f_object, fieldnames=field_names)

                  dictwriter_object.writerow(dict)

                  f_object.close()
