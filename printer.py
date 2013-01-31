from datetime import datetime, date, timedelta
import re


class LatexPrinter:
    def __init__(self, template=None):
        if template:
            self.template = file(template).readlines()
        else:
            self.template = None

    def print_day(self, start, end, pausestart, pauseend, worktime):
        print(start.strftime('%a, %d.%m.%Y & %H:%M & ') +
              end.strftime('%H:%M & ') +
              pausestart.strftime('%H:%M & ') +
              pauseend.strftime('%H:%M & ') +
              str(worktime.seconds/3600) + ":" + 
              str(worktime.seconds/60%60).zfill(2) + '\\\\')

    def print_week(self, weeknum, ndays, hours_per_day):
        time = timedelta(hours = ndays*hours_per_day)
        print('Summe KW ' + str(weeknum) + ' &&&&& ' + 
              str(time.seconds/3600 + time.days*24) + ":" + 
              str(time.seconds/60%60).zfill(2) + '\\\\')

    def print_month(self, name, ndays, hours_per_day):
        time = ndays*hours_per_day
        print('Summe ' + str(name) + ' &&&&& ' + str(time) + '\\\\')

    def print_divider(self):
        print('\\hline')

    def print_header(self):
        if self.template:
            for l in self.template:
                if re.search('#TIMETABLE#', l):
                    break
                l = re.sub('#MONTH#', date.today().strftime('%B, %Y'), l)
                print(l)
        else:
            print(' day & start & end & from & till\\\\')

    def print_footer(self):
        if self.template:
            do_print = False
            for l in self.template:
                if do_print:
                    print(l)
                if re.search('#TIMETABLE#', l):
                    do_print = True


class TextPrinter:
    def __init__(self):
        pass

    def print_day(self, start, end, pausestart, pauseend, worktime):
        print(start.strftime('%a, %d.%m.%Y | %H:%M | ') +
              end.strftime('%H:%M | ') + pausestart.strftime('%H:%M | ') +
              pauseend.strftime('%H:%M'))

    def print_week(self, weeknum, ndays, hours_per_day):
        time = ndays*hours_per_day
        print('week ' + str(weeknum) + ': ' + str(time))

    def print_month(self, name, ndays, hours_per_day):
        time = ndays*hours_per_day
        print('sum ' + str(name) + ': ' + str(time))

    def print_divider(self):
        print('----------------+-------+-------+-------+-------')

    def print_header(self):
        print('')
        print(' Worksheet ')
        print('"""""""""""')
        print('')
        print('Month: ' + date.today().strftime('%B, %Y'))
        print('')
        print('                                      pause')
        print(' day            | start |  end  | from  | till')

    def print_footer(self):
        print('')
        print('')
        print('')
        print('                   ____________________________')
        print('                   Date, Signature')
