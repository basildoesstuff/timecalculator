def add_time(start, duration, *day):

    start_h, start_m, period = start.replace(':',' ').replace(',', ',').split()
    duration_h, duration_m = duration.split(':')
    start_in_minutes = int(start_m) + (int(start_h) * 60)
    duration_in_minutes = int(duration_m) + (int(duration_h) * 60)
    total_minutes = start_in_minutes + duration_in_minutes

    def new_hours(minutes):
    
        new_hour = (minutes // 60) % 12
        if new_hour == 0:
            new_hour = 12
        
        return new_hour
    
    new_h = new_hours(total_minutes)
 
    def new_minutes(minutes):
        
        new_minute = (minutes % 60)
        if new_minute < 10:
            new_minute = '0' + str(new_minute)
        else:
            new_minute = str(new_minute)
       
        return new_minute
    
    new_m = new_minutes(total_minutes)
    
    
    def new_period(p):

        if p == 'PM' and (total_minutes // 720) % 2 == 0:
            new_per = 'PM'
        elif p == 'AM' and (total_minutes // 720) % 2 == 1:
            new_per = 'PM'
        else:
            new_per = 'AM'
        return new_per
        
    new_p = new_period(period)
 
    def count_days(p):
    
        if p == 'PM' and int(start_h) == 12:
            n_day = (total_minutes // 1440)
        elif p == 'PM' and int(start_h) < 12:
            if int(total_minutes) < 720:
                n_day = 0
            else:
                n_day = (total_minutes // 1440) + 1
        elif p == 'AM':
            n_day = (total_minutes // 1440)

        return n_day
    
    n_day = count_days(period)
 
    def days_pass(days):            
        
        if days == 1:
            passed = '(next day)'
        elif days >= 2:
            passed = '(' + str(n_day) + ' days later)'
        elif days == 0:
            passed = ''
        return passed
    
    d_pass = days_pass(n_day)

    def week_day(d):
        
        if d:
            d = str(*day).title()
          
            week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            idx = [i for i, n in enumerate(week) if n == d]  
            if idx:
                idx = idx[0]
            else:
                idx = 0

            n_day_idx = 0
            if int(n_day) == int(idx):
                n_day_idx = int(idx)
            elif int(n_day) >= 7 and int(n_day) >= idx:
                n_day_idx = int(idx) - int(n_day // 7 - 1)
            elif n_day < 7 and n_day < 6:
                n_day_idx = (n_day + idx) % 7
            else:
                n_day_idx = int(idx) + int(n_day)
            
            
            new_day = week[n_day_idx]
        else:
            new_day = ''
        
        return new_day
        
    new_d = week_day(day)

    def results(new_h, new_m, new_p, d_pass, new_d):
 
        if d_pass and new_d:
            
            new_time = str(new_h) + ':' + str(new_m) + ' ' + str(new_p) + ', ' + str(new_d) + ' ' + str(d_pass)
        elif d_pass != '' and new_d == '':
            
            new_time = str(new_h) + ':' + str(new_m) + ' ' + str(new_p) + ' ' + str(d_pass)
        elif new_d != '' and d_pass == '':
          
            new_time = str(new_h) + ':' + str(new_m) + ' ' + str(new_p) + ', ' + str(new_d)
        else:
          
            new_time = str(new_h) + ':' + str(new_m) + ' ' + str(new_p)
        return new_time
          
    new_time = results(new_h, new_m, new_p, d_pass, new_d)

    return new_time