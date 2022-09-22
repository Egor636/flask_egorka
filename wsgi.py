# gruup = {1:'ПРи201' 2: 'ПИ-201' }
GROUP = 2
if  GROUP == 1:
    from apppri import app
elif GROUP == 2:
    from apppi import app


if __name__ == '__main__':
    app.run(debug=True)