import tkinter as tk


def createWindow(title, width, height):
    window = tk.Tk()
    window.title(title)
    window.geometry('{}x{}'.format(width, height))
    return window


def computeArithmetic(num1, num2):

    num1 = int(num1)
    num2 = int(num2)
    if num1 < 0:
        raise ValueError('{} should larger than 0'.format(num1))
    if num2 < 0:
        raise ValueError('{} should larger than 0'.format(num2))
    result = ''
    result += '{} + {} = {}\n'.format(num1, num2, num1 + num2)
    result += '{} - {} = {}\n'.format(num1, num2, num1 - num2)
    result += '{} * {} = {}\n'.format(num1, num2, num1 * num2)
    result += '{} / {} = {}\n'.format(num1, num2, num1 / num2)
    return result


def drawArithmetic(mesg, num1, num2):
    try:
        result = computeArithmetic(num1, num2)
    except ValueError as e:
        result = str(e)
    mesg.set(result)


def main():
    # compuation_result = tk.StringVar()
    # compuation_result.set('123')
    window = createWindow('main', 600, 500)
    compuation_result = tk.StringVar()
    tk.Label(window, text="First Number").grid(row=0)
    tk.Label(window, text="Second Number").grid(row=1)

    first_nubmer_entry = tk.Entry(window)
    second_nubmer_entry = tk.Entry(window)

    first_nubmer_entry.grid(row=0, column=1)
    second_nubmer_entry.grid(row=1, column=1)
    msg = tk.Message(window, textvariable=compuation_result)
    msg.grid(row=3, column=1)
    button = tk.Button(
        window, text='Quit', command=window.quit).grid(
            row=2, column=1)
    button = tk.Button(
        window,
        text='cal',
        command=
        lambda: drawArithmetic(compuation_result, first_nubmer_entry.get(), second_nubmer_entry.get())
    ).grid(
        row=2, column=2)
    #tk.Button(window, text='calculate', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
    ## var = tk.StringVar()
    # text = tk.Label(
    #     window,
    #     text='OMG! this is TK!',
    #     bg='green',
    #     font=('Arial', 12),
    #     width=15,
    #     height=2)
    # text.pack()
    # text = tk.Label(
    #     window,
    #     textvariable=var,
    #     bg='green',
    #     font=('Arial', 12),
    #     width=15,
    #     height=2)
    # text.pack(side='left')

    # button = tk.Button(window, text='Stop', width=25, command=root.destroy)
    # button.pack()
    window.mainloop()


if __name__ == '__main__':
    main()