import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter.messagebox
from tkinter import *
from tkinter.ttk import *
from tkinter.font import Font
import os

data = pd.read_csv("matches data.csv")

data2008 = data[data['season'] == 2008]
data2009 = data[data['season'] == 2009]
data2010 = data[data['season'] == 2010]
data2011 = data[data['season'] == 2011]
data2012 = data[data['season'] == 2012]
data2013 = data[data['season'] == 2013]
data2014 = data[data['season'] == 2014]
data2015 = data[data['season'] == 2015]
data2016 = data[data['season'] == 2016]
data2017 = data[data['season'] == 2017]
data2018 = data[data['season'] == 2018]
data2019 = data[data['season'] == 2019]

before_rows = data.shape
# print(before_rows)

del data['umpire3']
data.dropna(inplace=True)

after_rows = data.shape
# print(after_rows)

# PRCENTAGE WIN MAIN


def percentage_match_win():
    (data.winner.value_counts(normalize=True)*100).plot(kind='barh', title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()

# SUBPART


def percentage_match_win_2008():
    (data2008.winner.value_counts(normalize=True)*100).plot(kind='barh', title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()


def percentage_match_win_2009():
    (data2009.winner.value_counts(normalize=True)*100).plot(kind='barh', title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()


def percentage_match_win_2010():
    (data2010.winner.value_counts(normalize=True)*100).plot(kind='barh', title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()


def percentage_match_win_2011():
    (data2011.winner.value_counts(normalize=True)*100).plot(kind='barh', title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()


def percentage_match_win_2012():
    (data2012.winner.value_counts(normalize=True)*100).plot(kind='barh', title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()


def percentage_match_win_2013():
    (data2013.winner.value_counts(normalize=True)*100).plot(kind='barh', title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()


def percentage_match_win_2014():
    (data2014.winner.value_counts(normalize=True)*100).plot(kind='barh', title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()


def percentage_match_win_2015():
    (data2015.winner.value_counts(normalize=True)*100).plot(kind='barh', title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()


def percentage_match_win_2016():
    (data2016.winner.value_counts(normalize=True)*100).plot(kind='barh',  title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()


def percentage_match_win_2017():
    (data2017.winner.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()


def percentage_match_win_2018():
    (data2018.winner.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()


def percentage_match_win_2019():
    (data2019.winner.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of matches won by Teams', figsize=(10, 5))
    plt.show()


def percent_clicked():

    yr = combo.get()
    if yr == '2008':
        percentage_match_win_2008()

    elif yr == '2009':
        percentage_match_win_2009()
    elif yr == '2010':
        percentage_match_win_2010()
    elif yr == '2011':
        percentage_match_win_2011()
    elif yr == '2012':
        percentage_match_win_2012()
    elif yr == '2013':
        percentage_match_win_2013()
    elif yr == '2014':
        percentage_match_win_2014()
    elif yr == '2015':
        percentage_match_win_2015()
    elif yr == '2016':
        percentage_match_win_2016()
    elif yr == '2017':
        percentage_match_win_2017()
    elif yr == '2018':
        percentage_match_win_2018()
    elif yr == '2019':
        percentage_match_win_2019()
    elif yr == 'overall':
        percentage_match_win()
    else:
        tkinter.messagebox.showinfo("Warning", "Select any one")
        print("Select any one")


#######################################################################################################################################################


# PRCENTAGE MATCH PLLAYED IN CITIES MAIN


def percentage_match_in_cities():
    (data.city.value_counts(normalize=True) * 100).plot(kind='pie', title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))

# SUBPART


def percentage_match_in_cities_2008():
    (data2008.city.value_counts(normalize=True) * 100).plot(kind='pie', title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))
    plt.show()


def percentage_match_in_cities_2009():
    (data2009.city.value_counts(normalize=True) * 100).plot(kind='pie', title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))
    plt.show()


def percentage_match_in_cities_2010():
    (data2010.city.value_counts(normalize=True) * 100).plot(kind='pie', title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))
    plt.show()


def percentage_match_in_cities_2011():
    (data2011.city.value_counts(normalize=True) * 100).plot(kind='pie', title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))
    plt.show()


def percentage_match_in_cities_2012():
    (data2012.city.value_counts(normalize=True) * 100).plot(kind='pie', title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))
    plt.show()


def percentage_match_in_cities_2013():
    (data2013.city.value_counts(normalize=True) * 100).plot(kind='pie', title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))
    plt.show()


def percentage_match_in_cities_2014():
    (data2014.city.value_counts(normalize=True) * 100).plot(kind='pie', title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))
    plt.show()


def percentage_match_in_cities_2015():
    (data2015.city.value_counts(normalize=True) * 100).plot(kind='pie', title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))
    plt.show()


def percentage_match_in_cities_2016():
    (data2016.city.value_counts(normalize=True) * 100).plot(kind='pie', title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))
    plt.show()


def percentage_match_in_cities_2017():
    (data2017.city.value_counts(normalize=True) * 100).plot(kind='pie', title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))
    plt.show()


def percentage_match_in_cities_2018():
    (data2018.city.value_counts(normalize=True) * 100).plot(kind='pie',  title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))
    plt.show()


def percentage_match_in_cities_2019():
    (data2019.city.value_counts(normalize=True) * 100).plot(kind='pie',  title='Percentage Of Matches Played in Cities(All Seasons)', figsize=(10, 5))
    plt.show()


def clicked_cities():
    yr2 = combo2.get()
    if yr2 == '2008':
        percentage_match_in_cities_2008()
    elif yr2 == '2009':
        percentage_match_in_cities_2009()
    elif yr2 == '2010':
        percentage_match_in_cities_2010()
    elif yr2 == '2011':
        percentage_match_in_cities_2011()
    elif yr2 == '2012':
        percentage_match_in_cities_2012()
    elif yr2 == '2013':
        percentage_match_in_cities_2013()
    elif yr2 == '2014':
        percentage_match_in_cities_2014()
    elif yr2 == '2015':
        percentage_match_in_cities_2015()
    elif yr2 == '2016':
        percentage_match_in_cities_2016()
    elif yr2 == '2017':
        percentage_match_in_cities_2017()
    elif yr2 == '2018':
        percentage_match_in_cities_2018()
    elif yr2 == '2019':
        percentage_match_in_cities_2019()
    elif yr2 == 'overall':
        percentage_match_in_cities()
    else:
        tkinter.messagebox.showinfo("Warning", "Select any one")
        print("Select any one")
####################################################################################################################################################


# PRCENTAGE TOSS WIN MAIN


def percentage_toss_win():
    (data.toss_decision.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of toss decisions(All Seasons)')
    plt.show()

# SUBPART


def percentage_toss_win_2008():
    (data2008.toss_decision.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of toss decisions(All Seasons)')
    plt.show()


def percentage_toss_win_2009():
    (data2009.toss_decision.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of toss decisions(All Seasons)')
    plt.show()


def percentage_toss_win_2010():
    (data2010.toss_decision.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of toss decisions(All Seasons)')
    plt.show()


def percentage_toss_win_2011():
    (data2011.toss_decision.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of toss decisions(All Seasons)')
    plt.show()


def percentage_toss_win_2012():
    (data2012.toss_decision.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of toss decisions(All Seasons)')
    plt.show()


def percentage_toss_win_2013():
    (data2013.toss_decision.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of toss decisions(All Seasons)')
    plt.show()


def percentage_toss_win_2014():
    (data2014.toss_decision.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of toss decisions(All Seasons)')
    plt.show()


def percentage_toss_win_2015():
    (data2015.toss_decision.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of toss decisions(All Seasons)')
    plt.show()


def percentage_toss_win_2016():
    (data2016.toss_decision.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of toss decisions(All Seasons)')
    plt.show()


def percentage_toss_win_2017():
    (data2017.toss_decision.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of toss decisions(All Seasons)')
    plt.show()


def percentage_toss_win_2018():
    (data2018.toss_decision.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of toss decisions(All Seasons)')
    plt.show()


def percentage_toss_win_2019():
    (data2019.toss_decision.value_counts(normalize=True) * 100).plot(kind='barh', title='Percentage of toss decisions(All Seasons)')
    plt.show()


def clicked_toss():
    yr3 = combo3.get()
    if yr3 == '2008':
        percentage_toss_win_2008()
    elif yr3 == '2009':
        percentage_toss_win_2009()
    elif yr3 == '2010':
        percentage_toss_win_2010()
    elif yr3 == '2011':
        percentage_toss_win_2011()
    elif yr3 == '2012':
        percentage_toss_win_2012()
    elif yr3 == '2013':
        percentage_toss_win_2013()
    elif yr3 == '2014':
        percentage_toss_win_2014()
    elif yr3 == '2015':
        percentage_toss_win_2015()
    elif yr3 == '2016':
        percentage_toss_win_2016()
    elif yr3 == '2017':
        percentage_toss_win_2017()
    elif yr3 == '2018':
        percentage_toss_win_2018()
    elif yr3 == '2019':
        percentage_toss_win_2019()

    elif yr3 == 'overall':
        percentage_toss_win()
    else:
        tkinter.messagebox.showinfo("Warning", "Select any one")
        print("Select any one")


####################################################################################################################################################


# MAN OF THE MATCH MAIN


def max_manofthematch():
    data.player_of_match.value_counts().head().plot(kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)
    plt.show()

# SUBPART


def max_manofthematch_2008():
    data2008.player_of_match.value_counts().head().plot(kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)
    plt.show()


def max_manofthematch_2009():
    data2009.player_of_match.value_counts().head().plot(kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)
    plt.show()


def max_manofthematch_2010():
    data2010.player_of_match.value_counts().head().plot(kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)
    plt.show()


def max_manofthematch_2011():
    data2011.player_of_match.value_counts().head().plot(kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)
    plt.show()


def max_manofthematch_2012():
    data2012.player_of_match.value_counts().head().plot(kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)
    plt.show()


def max_manofthematch_2013():
    data2013.player_of_match.value_counts().head().plot(kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)
    plt.show()


def max_manofthematch_2014():
    data2014.player_of_match.value_counts().head().plot(kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)
    plt.show()


def max_manofthematch_2015():
    data2015.player_of_match.value_counts().head().plot(kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)
    plt.show()


def max_manofthematch_2016():
    data2016.player_of_match.value_counts().head().plot(kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)
    plt.show()


def max_manofthematch_2017():
    data2017.player_of_match.value_counts().head().plot(kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)


def max_manofthematch_2018():
    data2018.player_of_match.value_counts().head().plot(kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)


def max_manofthematch_2019():
    data2019.player_of_match.value_counts().head().plot(kind='barh', title="Top Players Become max times--\'Man of The Match'", grid=True)


def clicked_mtm():
    yr4 = combo4.get()
    if yr4 == '2008':
        max_manofthematch_2008()
    elif yr4 == '2009':
        max_manofthematch_2009()
    elif yr4 == '2010':
        max_manofthematch_2010()
    elif yr4 == '2011':
        max_manofthematch_2011()
    elif yr4 == '2012':
        max_manofthematch_2012()
    elif yr4 == '2013':
        max_manofthematch_2013()
    elif yr4 == '2014':
        max_manofthematch_2014()
    elif yr4 == '2015':
        max_manofthematch_2015()
    elif yr4 == '2016':
        max_manofthematch_2016()
    elif yr4 == '2017':
        max_manofthematch_2017()
    elif yr4 == '2018':
        max_manofthematch_2018()
    elif yr4 == '2019':
        max_manofthematch_2019()
    elif yr4 == 'overall':
        max_manofthematch()
    else:
        tkinter.messagebox.showinfo("Warning","Select any one")
        print("select any one")


####################################################################################################################################################

# OVERALL FAVOURITE VENUE


def favourite_venue():
    data.venue.value_counts().plot(kind='bar', title='Fav Grounds', figsize=(15, 8), grid=(15, 8)).legend(bbox_to_anchor=(1.2, 0.5))
    plt.show()
# SUBPART  DONT REQUIRE


####################################################################################################################################################


# MATCHES WIN BY VENUES


def venue_win_1():
    chinna_win = data[data.venue == 'M Chinnaswamy Stadium']['winner'].value_counts(normalize=True)*100
    chinna_win.plot(kind='line', title='winning percent at Chinnaswamy', figsize=(10, 5), grid=True).legend(bbox_to_anchor=(1.2, 0.5))
    plt.show()


def venue_win_2():
    Eden_win = data[data.venue == 'Eden Gardens']['winner'].value_counts(normalize=True)*100
    Eden_win.plot(kind='line', title='winning percent at Eden Gardens', figsize=(10, 5), grid=True).legend(bbox_to_anchor=(1.2, 0.5))
    plt.show()


def venue_win_3():
    Rajiv_win = data[data.venue == 'Rajiv Gandhi International Stadium, Uppal']['winner'].value_counts(normalize=True)*100
    Rajiv_win.plot(kind='line', title='winning percent at Rajiv Gandhi International Stadium, Uppal', figsize=(10, 5), grid=True).legend(bbox_to_anchor=(1.2, 0.5))
    plt.show()


def venue_win_4():
    Wan_win = data[data.venue == 'Wankhede Stadium']['winner'].value_counts(normalize=True)*100
    Wan_win.plot(kind='line', title='winning percent at Wankhede Stadium', figsize=(10, 5), grid=True).legend(bbox_to_anchor=(1.2, 0.5))
    plt.show()


def venue_win_5():
    Kotla_win = data[data.venue == 'Feroz Shah Kotla']['winner'].value_counts(normalize=True)*100
    Kotla_win.plot(kind='line', title='winning percent at Feroz Shah Kotla', figsize=(10, 5), grid=True).legend(bbox_to_anchor=(1.2, 0.5))
    plt.show()


def venue_win_6():
    Chepauk_win = data[data.venue == 'MA Chidambaram Stadium, Chepauk']['winner'].value_counts(normalize=True)*100
    Chepauk_win.plot(kind='line', title='winning percent at MA Chidambaram Stadium, Chepauk', figsize=(10, 5), grid=True).legend(bbox_to_anchor=(1.2, 0.5))
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
        max_manofthematch()
    else:
        tkinter.messagebox.showinfo("Warning", "Select any one ")
        print("Select any one")
####################################################################################################################################################

# MAN OF THE MATCH MAIN


def decision_by_each_team():
    pd.crosstab(data.winner, data.toss_decision).plot(kind='bar', title='Winning w.r.t toss decisions overall', figsize=(10, 5))
    plt.show()

# SUBPART  NOT REQUIRED

####################################################################################################################################################

# MAN OF THE MATCH MAIN


# need to fix bug here
def bestplayer():
    pd.crosstab(data2019.player_of_match, data2019.season).plot(kind='barh', title='Player of match', figsize=(10, 8)).legend(bbox_to_anchor=(1.0, 0.5))
    plt.show()

# SUBPART  NOT REQUIRED

####################################################################################################################################################

# MAN OF THE MATCH MAIN


def winincities():
    pd.crosstab(data.winner, data.city).plot(kind='bar', title='Winning w.r.t cities in IPL', figsize=(10, 5))
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
win.geometry("1024x800")
win.minsize(1024, 800)
win.maxsize(1024, 800)

lb0 = Label(win, text="	IPL DATA ANALYSIS", background="Black", foreground="#F9F", font=("Times",27), width=39)
lb0.grid(columnspan=4, padx=10, pady=10)

#********** Run made

lbl01 = Label(win, text="Run made", width=25, relief="sunken", background="purple", foreground="White", font=("Times", 12))
lbl01.grid(row=10, column=0, padx=7, pady=7)

btn9 = Button(win, text="Show info", command=percent_clicked, width=25)
btn9.grid(row=13, column=0, padx=7, pady=7)

combo10 = Combobox(win, width=25)
combo10['values'] = ('Select Player', 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019)
combo10.current(0)  # set the selected item
combo10.grid(row=11, column=0, padx=7, pady=7)

combo9 = Combobox(win, width=25)
combo9['values'] = ('Select Year', 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019)
combo9.current(0)  # set the selected item
combo9.grid(row=12, column=0, padx=7, pady=7)


# ********* % of Match win

lbl1 = Label(win, text="   Match Winning %", width=25, relief="sunken", background="purple", foreground="White", font=("Times", 12))
lbl1.grid(row=1, column=0, padx=7, pady=7)

btn1 = Button(win, text="Show graph", command=percent_clicked, width=25)
btn1.grid(row=3, column=0, padx=7, pady=7)

combo = Combobox(win, width=25)
combo['values'] = ('Select Year', 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 'overall')
combo.current(0)  # set the selected item
combo.grid(row=2, column=0, padx=7, pady=7)

# ***********  % of match played in cities


lbl2 = Label(win, text='% of Match played in cities', width=25, relief="sunken", background="purple", foreground="White", font=("Times", 12))
lbl2.grid(row=1, column=1, padx=7, pady=7)

combo2 = Combobox(win, width=25)
combo2['values'] = ('Select Year', 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 'overall')
combo2.current(0)  # set the selected item
combo2.grid(row=2, column=1, padx=7, pady=7)

btn2 = Button(win, text="Show graph", command=clicked_cities, width=25)
btn2.grid(row=3, column=1, padx=7, pady=7)

# ************* %  Toss Win Main

lbl3 = Label(win, text=' % of Toss Win', width=25, relief="ridge", background="purple", foreground="White", font=("Times", 12))
lbl3.grid(row=1, column=2, padx=7, pady=7)

combo3 = Combobox(win, width=25)
combo3['values'] = ('Select Year', 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 'overall')
combo3.current(0)  # set the selected item
combo3.grid(row=2, column=2, padx=7, pady=7)

btn3 = Button(win, text="Show graph", command=clicked_toss, width=25)
btn3.grid(row=3, column=2, padx=7, pady=7)

# ********** Man of the Match

lbl3 = Label(win, text='Man of The Match', width=25, relief="ridge", background="purple", foreground="White", font=("Times", 12))
lbl3.grid(row=5, column=0, padx=7, pady=7)

combo4 = Combobox(win, width=25)
combo4['values'] = ('Select Year', 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 'overall')
combo4.current(0)  # set the selected item
combo4.grid(row=6, column=0, padx=7, pady=7)

btn4 = Button(win, text="Show graph", command=clicked_mtm, width=25)
btn4.grid(row=7, column=0, padx=7, pady=7)

# ********* Matches win by Venue

lbl4 = Label(win, text='Match win by venue', width=25, relief="ridge", background="purple", foreground="White", font=("Times", 12))
lbl4.grid(row=5, column=1, padx=7, pady=7)

combo5 = Combobox(win, width=25)
combo5['values'] = ('Select Venue', 'M Chinnaswamy Stadium', 'Eden Gardens', 'Rajiv Gandhi International Stadium', 'Wankhede Stadium', 'Feroz Shah Kotla', 'MA Chidambaram Stadium', 'overall')
combo5.current(0)  # set the selected item
combo5.grid(row=6, column=1, padx=7, pady=7)

btn5 = Button(win, text="Show graph", command=clicked_Venue, width=25)
btn5.grid(row=7, column=1, padx=7, pady=7)

btn6 = Button(win, text='Decisions of teams', command=decision_by_each_team, width=25)
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
