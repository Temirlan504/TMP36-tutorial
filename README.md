# TMP36 Tutorial using MicroPython
### Описание проекта на русском, смотри ниже ↓
### Қазақ тілінде проекттің сипаттамасы төменде көр ↓
---

This tutorial will show you how to use the [TMP36](https://www.analog.com/media/en/technical-documentation/data-sheets/tmp35_36_37.pdf) analog temperature sensor with MicroPython and Tiny2040 (Raspberry Pi Pico). The TMP36 provides a voltage output ***linearly proportional*** to the Celsius temperature, allowing us to use the equation of a line *y = mx + b* for temperature calculations.

### Hardware Required
1. Raspberry Pi Pico or Tiny2040
2. TMP36 Temperature Sensor
3. Breadboard
4. Jumper Wires

### Circuit Diagram

![TMP36 Circuit Diagram](tmp36_circuit_diagram.png)

Using the TMP36 datasheet, we see the sensor pins as follows:

![TMP36 Pinout](tmp36_pinout.png)

With the legs facing you, the left pin is the voltage pin, the middle pin is the output voltage, and the right pin is the ground pin.

Connect the output voltage pin to the ADC pin (GP26) of the Tiny2040. Connect the voltage pin to the 3.3V (as the datasheet specifies testing under 3V of power), and the ground pin to the GND pin of the Raspberry Pi Pico.

### Deriving the Formula for Temperature Calculation
The TMP36 sensor provides an output voltage linearly proportional to the Celsius temperature. Using the equation of a line "y = mx + b", we can calculate the temperature:
- y = Temperature in Celsius
- m = Slope of the line = (y2 - y1) / (x2 - x1)
- x = Output voltage of the sensor
- b = Y-intercept (calculated later)

The TMP36 datasheet provides the following graph:

![TMP36 Graph](tmp36_graph.png)

From the graph, we can take any two points (x1, y1) and (x2, y2) to calculate the slope. For this example, we use the points (1V, 50°C) and (0.4V, -12.5°C).

Using the slope formula, we get:
\[ m = \frac{50 - (-12.5)}{1 - 0.4} = \frac{62.5}{0.6} = 104.1667 \]

Next, we calculate the y-intercept (b) by substituting the values of m, x, and y in the line equation. Using the point (1V, 50°C):
\[ 50 = 104.1667 \cdot 1 + b \]
\[ b = 50 - 104.1667 \]
\[ b = -54.1667 \]

So, the temperature calculation formula is:
\[ y = mx + b \]
\[ \text{Temperature} = 104.1667 \cdot \text{Output Voltage} + (-54.1667) \]

Now that the hardest part is done, we can use this formula in the code to get the temperature in Celsius.

### Code
[main.py](main.py)

---

В этом руководстве показано, как пользоваться аналоговым датчиком температуры [TMP36](https://www.analog.com/media/en/technical-documentation/data-sheets/tmp35_36_37.pdf) с MicroPython и Tiny2040 (Raspberry Pi Pico). TMP36 выдаёт выходное напряжение ***линейно пропорциональное*** температуре по цельсию, что позволяет нам использовать уравнение линии *y = kx + b* для расчетов температуры.

### Требуемое оборудование
1. Raspberry Pi Pico или Tiny2040.
2. Датчик температуры TMP36.
3. Макетная плата
4. Провода

### Принципиальная электрическая схема

![Схема TMP36](tmp36_circuit_diagram.png)

В даташите TMP36, мы видим распиновку датчика следующим образом:

![Распиновка TMP36](tmp36_pinout.png)

Ноги датчика смотрят на нас, тогда левый контакт — это контакт питания, средний контакт — выходное напряжение, а правый контакт — контакт заземления.

Подключите вывод выходного напряжения к выводу ADC0 (GP26). Подключите контакт напряжения к 3,3 В (потому-что в даташите указано тестирование при напряжении 3В), а контакт заземления — к контакту GND Raspberry Pi Pico.

### Вывод формулы для расчета температуры
Датчик TMP36 обеспечивает выходное напряжение, линейно пропорциональное температуре Цельсия. Используя уравнение линии «y = kx + b», мы можем рассчитать температуру:
- y = температура в градусах Цельсия
- k = Наклон линии = (y2 - y1) / (x2 - x1)
- x = Выходное напряжение датчика
- b = точка пересечения Y (посчитаем позже)

В дашите TMP36 представлен следующий график:

![График TMP36](tmp36_graph.png)

Из графика мы можем взять любые две точки (x1, y1) и (x2, y2) для расчета наклона. В этом примере мы используем точки (1В, 50°C) и (0,4В, -12,5°C).

Используя формулу наклона, получаем:
\[ k = \frac{50 - (-12,5)}{1 - 0,4} = \frac{62,5}{0,6} = 104,1667 \]

Затем мы вычисляем точку пересечения оси y (b), подставляя значения k, x и y в уравнение линии. Используя точку (1В, 50°C):

\[ 50 = 104,1667 \cdot 1 + b \]
\[ b = 50 - 104,1667 \]
\[ b = -54,1667 \]

Итак, формула расчета температуры такова:

\[ у = kx + b \]
\[ \text{Температура} = 104,1667 \cdot \text{Выходное напряжение} + (-54,1667) \]

Теперь, когда самое сложное сделано, мы можем использовать эту формулу в коде, чтобы получить температуру в градусах Цельсия.

### Код
[main.py](main.py)

---

Бұл нұсқаулықта [TMP36](https://www.analog.com/media/en/technical-documentation/data-sheets/tmp35_36_37.pdf) аналогды температура сенсорын MicroPython және Tiny2040 (Raspberry Pi Pico) пайдалану үшін қалай пайдалануға арналғанын көрсетемін. TMP36 Цельсий температурасына ***линейно пропорционально*** шығысты береді, сондықтан бізге температура есептемелері үшін *y = kx + b* теңдеуін пайдалануға мүмкіндік береді.

### Қажетті жабдықтар
1. Raspberry Pi Pico немесе Tiny2040.
2. TMP36 Температура Сенсоры.
3. Макет платасы
4. Сымдар

### Схема

![TMP36 Схемасы](tmp36_circuit_diagram.png)

TMP36 даташит пайдаланғанда, сенсордың распиновка көреміз:

![TMP36 Распиновка](tmp36_pinout.png)

Сенсордың аяқтар сізге қарағанда, сол жақты контакт — бұл питание, ортағағы контакт — шығыстық напряжение, оң жақты контакт — заземление контакты.

Шығыстық напряжение контактын Tiny2040-дың ADC контактына (GP26) қосыңыз. Питание контактын 3.3В-ға (даташитда 3В-да тексеру көрсетілгенін) қосыңыз, және заземление контактын Raspberry Pi Pico-ның GND контактына қосыңыз.

### Температураны есептеу формуласын шығару

TMP36 сенсоры Цельсий температурасына линейно-пропорциялы шығысты береді. Температураны сызықтық теңдеу арқылы есептеуге болады:
- y = Цельсий температурасы
- k = көлбеу бұрышы = (y2 - y1) / (x2 - x1)
- x = Сенсордың шығыстық напряжениясы
- b = Кейінге есептеледі

TMP36 даташит астында келесі графикті көрейік:

![TMP36 Графигі](tmp36_graph.png)

Графиктен көлбеуді (k) есептеу үшін кез келген екі нүктені (x1, y1) және (x2, y2) алуға болады. Бұл мысалда (1В, 50°C) және (0,4В, -12,5°C) нүктелерін қолданамыз.

Формуласын пайдалану арқылы, біз:
\[ k = \frac{50 - (-12.5)}{1 - 0.4} = \frac{62.5}{0.6} = 104.1667 \]

Келесі, b келесілікті есептеу арқылы табуымыз келеді. k, x және y-ның мәндерін линиялық теңдеу формуласында пайдалану арқылы. (1В, 50°C) пайдалану арқылы:

\[ 50 = 104.1667 \cdot 1 + b \]
\[ b = 50 - 104.1667 \]
\[ b = -54.1667 \]

Сондықтан, температура есептемесі формуласы:
\[ у = kx + b \]
\[ \text{Температура} = 104.1667 \cdot \text{Шығыстық Напряжение} + (-54.1667) \]

Енді, ең үлкен іс орындалған соң, біз бұл формуланы кодта пайдалану арқылы Цельсий температурасын алуға болады.

### Код
[main.py](main.py)
