import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *
from tkinter.ttk import *
import os

data = pd.read_csv("matches data.csv")

data2008 = data[data['season'] == 2008]

before_rows = data.shape
del data['umpire3']
data.dropna(inplace=True)

after_rows = data.shape

############################### PRCENTAGE WIN MAIN ###############################


def percentage_match_win(yr):
    if yr == 'overall':
        data1 = data
    else:
        data1 = data[data['season'] == int(yr)]

    (data1.winner.value_counts(normalize=True)*100).plot(kind='barh',
                                                         title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()


def percent_clicked():

    yr = combo.get()
    percentage_match_win(yr)

#######################################################################################################################################################


# PRCENTAGE MATCH PLLAYED IN CITIES MAIN


def percentage_match_in_cities(yr2):
    if yr2 == 'overall':
        data1 = data
    else:
        data1 = data[data['season'] == int(yr2)]
    (data1.city.value_counts(normalize=True) * 100).plot(kind='pie',
                                                         title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))


def clicked_cities():
    yr2 = combo2.get()
    percentage_match_in_cities(yr2)

#######################################################################################################################################################

# PRCENTAGE TOSS WIN MAIN


def percentage_toss_win(yr3):
    if yr3 == 'overall':
        data1 = data
    else:
        data1 = data[data['season'] == int(yr3)]

    (data1.toss_decision.value_counts(normalize=True)*100).plot(kind='barh',
                                                                title='Percentage of toss decisions(All Seasons)')
    plt.show()


def clicked_toss():
    yr3 = combo3.get()
    percentage_toss_win(yr3)

#######################################################################################################################################################

# MAN OF THE MATCH MAIN


def max_manofthematch(yr4):
    if yr4 == 'overall':
        data1 = data
    else:
        data1 = data[data['season'] == int(yr4)]

    data1.player_of_match.value_counts().head().plot(
        kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)
    plt.show()


def clicked_mtm():
    yr4 = combo4.get()
    max_manofthematch(yr4)

#######################################################################################################################################################


# MATCHES WIN BY VENUES


def venue_win_1():
    chinna_win = data[data.venue == 'M Chinnaswamy Stadium']['winner'].value_counts(
        normalize=True)*100
    chinna_win.plot(kind='line', title='winning percent at Chinnaswamy', figsize=(
        10, 5), grid=True).legend(bbox_to_anchor=(1.2, 0.5))
    plt.show()


def venue_win_2():
    Eden_win = data[data.venue == 'Eden Gardens']['winner'].value_counts(
        normalize=True)*100
    Eden_win.plot(kind='line', title='winning percent at Eden Gardens', figsize=(
        10, 5), grid=True).legend(bbox_to_anchor=(1.2, 0.5))
    plt.show()


def venue_win_3():
    Rajiv_win = data[data.venue == 'Rajiv Gandhi International Stadium, Uppal']['winner'].value_counts(
        normalize=True)*100
    Rajiv_win.plot(kind='line', title='winning percent at Rajiv Gandhi International Stadium, Uppal', figsize=(
        10, 5), grid=True).legend(bbox_to_anchor=(1.2, 0.5))
    plt.show()


def venue_win_4():
    Wan_win = data[data.venue == 'Wankhede Stadium']['winner'].value_counts(
        normalize=True)*100
    Wan_win.plot(kind='line', title='winning percent at Wankhede Stadium', figsize=(
        10, 5), grid=True).legend(bbox_to_anchor=(1.2, 0.5))
    plt.show()


def venue_win_5():
    Kotla_win = data[data.venue == 'Feroz Shah Kotla']['winner'].value_counts(
        normalize=True)*100
    Kotla_win.plot(kind='line', title='winning percent at Feroz Shah Kotla', figsize=(
        10, 5), grid=True).legend(bbox_to_anchor=(1.2, 0.5))
    plt.show()


def venue_win_6():
    Chepauk_win = data[data.venue == 'MA Chidambaram Stadium, Chepauk']['winner'].value_counts(
        normalize=True)*100
    Chepauk_win.plot(kind='line', title='winning percent at MA Chidambaram Stadium, Chepauk', figsize=(
        10, 5), grid=True).legend(bbox_to_anchor=(1.2, 0.5))
    plt.show()

# OVERALL FAVOURITE VENUE


def favourite_venue(yr5):
    if yr5 == 'overall':
        venue1 = data.venue
    else:
        data1 = data[data['season'] == yr5]

    data.venue1.value_counts().plot(kind='bar', title='Fav Grounds', figsize=(15, 8),
                                    grid=(15, 8)).legend(bbox_to_anchor=(1.2, 0.5))
    plt.show()


def clicked_Venue():
    yr5 = combo5.get()
    if yr5 == 'M Chinnaswamy Stadium':
        venue_win_1()
    elif yr5 == 'Eden Gardens':
        venue_win_2()
    elif yr5 == 'Rajiv Gandhi International Stadium':
        venue_win_3()
    elif yr5 == 'Wankhede Stadium':
        venue_win_4()
    elif yr5 == 'Feroz Shah Kotla':
        venue_win_5()
    elif yr5 == 'MA Chidambaram Stadium':
        venue_win_6()
    elif yr5 == 'overall':
        favourite_venue()
    else:
        print("Select any one")

#######################################################################################################################################################

# MAN OF THE MATCH MAIN


def decision_by_each_team():
    pd.crosstab(data.winner, data.toss_decision).plot(
        kind='bar', title='Winning w.r.t toss decisions overall', figsize=(10, 5))
    plt.show()

# SUBPART  NOT REQUIRED

####################################################################################################################################################

# MAN OF THE MATCH MAIN


# need to fix bug here
def bestplayer():
    pd.crosstab(data2019.player_of_match, data2019.season).plot(
        kind='barh', title='Player of match', figsize=(10, 8)).legend(bbox_to_anchor=(1.0, 0.5))
    plt.show()

# SUBPART  NOT REQUIRED

####################################################################################################################################################

# MAN OF THE MATCH MAIN


def winincities():
    pd.crosstab(data.winner, data.city).plot(
        kind='bar', title='Winning w.r.t cities in IPL', figsize=(10, 5))
    plt.show()


# SUBPART NOT REQUIRED

####################################################################################################################################################

# MAN OF THE MATCH MAIN


def fav_umpire():
    fav_umpire = data.umpire1.value_counts().head(10)
    plt.subplots(figsize=(10, 15))
    sns.barplot(x=fav_umpire.values, y=fav_umpire.index, palette="Blues_d")
    plt.show()


####################################################################################################################################################


# MAN OF THE MATCH MAIN


def max_tosswin():
    data.toss_winner.value_counts().plot(kind='bar')

# SUBPART  NOT REQUIRED

####################################################################################################################################################


win = Tk()

win.title("IPL DATA ANALYSIS")
win.configure(background="gray")
win.geometry("700x400")
win.minsize(700, 400)
win.maxsize(700, 400)

lb0 = Label(win, text="	IPL DATA ANALYSIS", background="Black",
            foreground="#F9F", font=("Times", 27), width=39)
lb0.grid(columnspan=4, padx=10, pady=10)


# ********* % of Match win

lbl1 = Label(win, text="   Match Winning %", width=25, relief="ridge",
             background="purple", foreground="White", font=("Times", 12))
lbl1.grid(row=1, column=0, padx=7, pady=7)

btn1 = Button(win, text="Show graph", command=percent_clicked, width=25)
btn1.grid(row=3, column=0, padx=7, pady=7)

combo = Combobox(win, width=25)
combo['values'] = ('select', 2008, 2009, 2010, 2011, 2012,
                   2013, 2014, 2015, 2016, 2017, 2018, 2019, 'overall')
combo.current(0)  # set the selected item
combo.grid(row=2, column=0, padx=7, pady=7)

# ***********  % of match played in cities


lbl2 = Label(win, text='% of Match played in cities', width=25, relief="ridge",
             background="purple", foreground="White", font=("Times", 12))
lbl2.grid(row=1, column=1, padx=7, pady=7)

combo2 = Combobox(win, width=25)
combo2['values'] = ('select', 2008, 2009, 2010, 2011, 2012,
                    2013, 2014, 2015, 2016, 2017, 2018, 2019, 'overall')
combo2.current(0)  # set the selected item
combo2.grid(row=2, column=1, padx=7, pady=7)

btn2 = Button(win, text="Show graph", command=clicked_cities, width=25)
btn2.grid(row=3, column=1, padx=7, pady=7)

# ************* %  Toss Win Main

lbl3 = Label(win, text=' % of Toss Win', width=25, relief="ridge",
             background="purple", foreground="White", font=("Times", 12))
lbl3.grid(row=1, column=2, padx=7, pady=7)

combo3 = Combobox(win, width=25)
combo3['values'] = ('select', 2008, 2009, 2010, 2011, 2012,
                    2013, 2014, 2015, 2016, 2017, 2018, 2019, 'overall')
combo3.current(0)  # set the selected item
combo3.grid(row=2, column=2, padx=7, pady=7)

btn3 = Button(win, text="Show graph", command=clicked_toss, width=25)
btn3.grid(row=3, column=2, padx=7, pady=7)

# ********** Man of the Match

lbl3 = Label(win, text='Man of The Match', width=25, relief="ridge",
             background="purple", foreground="White", font=("Times", 12))
lbl3.grid(row=5, column=0, padx=7, pady=7)

combo4 = Combobox(win, width=25)
combo4['values'] = ('select', 2008, 2009, 2010, 2011, 2012,
                    2013, 2014, 2015, 2016, 2017, 2018, 2019, 'overall')
combo4.current(0)  # set the selected item
combo4.grid(row=6, column=0, padx=7, pady=7)

btn4 = Button(win, text="Show graph", command=clicked_mtm, width=25)
btn4.grid(row=7, column=0, padx=7, pady=7)

# ********* Matches win by Venue

lbl4 = Label(win, text='Match win by venue', width=25, relief="ridge",
             background="purple", foreground="White", font=("Times", 12))
lbl4.grid(row=5, column=1, padx=7, pady=7)

combo5 = Combobox(win, width=25)
combo5['values'] = ('select', 'M Chinnaswamy Stadium', 'Eden Gardens', 'Rajiv Gandhi International Stadium',
                    'Wankhede Stadium', 'Feroz Shah Kotla', 'MA Chidambaram Stadium', 'overall')
combo5.current(0)  # set the selected item
combo5.grid(row=6, column=1, padx=7, pady=7)

btn5 = Button(win, text="Show graph", command=clicked_Venue, width=25)
btn5.grid(row=7, column=1, padx=7, pady=7)

btn6 = Button(win, text='Decisions of teams',
              command=decision_by_each_team, width=25)
btn6.grid(row=6, column=2, padx=7, pady=7)

btn7 = Button(win, text='Fav Umpire', command=fav_umpire, width=25)
btn7.grid(row=9, column=0, padx=7, pady=7)

btn7 = Button(win, text='Fav City', command=winincities, width=25)
btn7.grid(row=9, column=1, padx=7, pady=7)

btn7 = Button(win, text='Max Toss Win', command=max_tosswin, width=25)
btn7.grid(row=9, column=2, padx=7, pady=7)

btn7 = Button(win, text='Best Player', command=bestplayer, width=25)
btn7.grid(row=7, column=2, padx=7, pady=7)

lab = Label

win.mainloop()
