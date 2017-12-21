import tkinter as tk


def createWindow(title, width, height):
    window = tk.Tk()
    window.title(title)
    window.geometry('{}x{}'.format(width, height))
    return window


def square(length, width):
    return length * width


def feetTometherArea(feet_area):
    return feet_area * 0.09290304


def meterToFeetArea(meter_area):
    return meter_area / 0.09290304


def strToPostiveNumber(n):
    try:
        number = int(n)
    except ValueError:
        raise ValueError('the value {} can not convert to integer'.format(n))

    if number < 0:
        raise ValueError('the value {} is must larger than 0'.format(n))

    return number


def answer(length, width, unit):
    result = ''
    result += 'You entered dimensions of {length} {unit} by {width} {unit}.\n'.format(
        length=length, width=width, unit=unit)

    result += 'The area is\n'

    area = square(length, width)
    if unit == 'meter':
        result += '{} square methers\n'.format(area)
        result += '{} square feet\n'.format(meterToFeetArea(area))
    else:
        result += '{} square feet\n'.format(area)
        result += '{} square methers\n'.format(feetTometherArea(area))
    return result


def callback(length_widget, width_widget, unit_widget, message_widget):
    convert_success = True
    try:
        length = strToPostiveNumber(length_widget.get())
        width = strToPostiveNumber(width_widget.get())
    except ValueError as e:
        message_widget.set(e)
        convert_success = False
    if convert_success:
        unit = unit_widget.get()
        message_widget.set(answer(length, width, unit))


def main():
    # compuation_result = tk.StringVar()
    # compuation_result.set('123')
    window = createWindow('main', 600, 500)

    tk.Label(window, text="Length:").grid(row=0)
    length_var = tk.StringVar()
    length = tk.Entry(window, textvariable=length_var)
    length.grid(row=0, column=1)

    tk.Label(window, text="Width:").grid(row=1)
    width_var = tk.StringVar()
    width = tk.Entry(window, textvariable=width_var)
    width.grid(row=1, column=1)

    tk.Label(window, text="Unit:").grid(row=2)
    choices = ['meter', 'feet']
    unit_var = tk.StringVar(window)
    unit_var.set(choices[0])
    unit_widget = tk.OptionMenu(window, unit_var, *choices)
    unit_widget.grid(row=2, column=1)

    tk.Label(window, text="Message:").grid(row=3)
    msg_var = tk.StringVar(window)
    msg = tk.Message(window, textvariable=msg_var)
    msg.grid(row=3, column=1)

    length_var.trace(
        'w',
        lambda name, index, mode: callback(length_var, width_var, unit_var, msg_var)
    )
    width_var.trace(
        'w',
        lambda name, index, mode: callback(length_var, width_var, unit_var, msg_var)
    )

    unit_var.trace(
        'w',
        lambda name, index, mode: callback(length_var, width_var, unit_var, msg_var)
    )

    window.mainloop()


if __name__ == '__main__':
    main()