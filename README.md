# Представление изображений в n-мерном векторном пространстве

## 1. Цель лабораторной работы
Приобретение и закрепление знаний и получение практических навыков работы с простейшими алгоритмами распознавания на основе представления изображений в виде точек в n-мерном векторном пространстве.

## 2. Краткие сведения из теории
### 2.1. Представление изображений в векторной форме
Существует большое число различных форм представления изображений в распознающих устройствах или программах. Одной из наиболее простых и понятных является форма, использующая представление изображений в виде точек в некотором n-мерном пространстве. Каждая ось такого пространства естественным образом соотносится с одним из n входов или с одним из n рецепторов распознающей системы. Каждый из рецепторов может находиться в одном из m состояний, если они дискретны, или иметь бесконечно большое число состояний, если рецепторы непрерывны. В зависимости от вида используемых рецепторов может порождаться непрерывное, дискретное или непрерывно-дискретное n-мерное пространство.
Как правило, в пространстве изображений вводится метрика – функция, которая каждой упорядоченной паре точек x и y пространства ставит в соответствие действительное число d(x, y). При этом функция d(x, y) обладает следующими свойствами:
1) ,  тогда и только тогда, когда x = y;
2) ;
3) .
Введение метрики d(x, y) в пространстве изображений позволяет говорить о близости или удаленности точек в этом пространстве или о мере сходства или различия анализируемых изображений. Понятие меры сходства изображений широко используется в теории распознавания образов. Однако формализация этого понятия при решении конкретных задач распознавания не является тривиальной задачей. Более того, эта задача является одной из основных задач теории распознавания образов. Рассмотрим общие требования к мере сходства изображений.
Пусть задано некоторое конечное множество  входных изображений, каждое из которых является точкой в n-мерном пространстве изображений. Меру сходства изображений можно ввести как функцию двух аргументов , где . Общие требования к этой функции можно свести к следующему:
1) функция  должна обладать свойством симметрии, т.е.
;
2) область значений функции  – множество неотрицательных чисел, т.е.
,   k, i = 1, 2,…, n;
3) мера сходства изображения с самим собой должна принимать экстремальное значение по сравнению с любым другим изображением, т.е в зависимости от способа введения меры сходства должно выполняться одно из двух соотношений:
,
;
4) в случае непрерывного n-мерного пространства и компактных образов функция  должна быть монотонной функцией удаления точек Sk и Si друг от друга в этом пространстве.
Анализ свойств метрики и меры сходства изображений показывает, что требования к функции  нетрудно выполнить в метрических пространствах. В частности, если в метрическом пространстве введено расстояние, то оно может быть использовано в виде меры сходства изображений. 

### 2.2. Распознавание по расстояниям в n-мерном пространстве
Эталонные изображения X1, X2,…, Xm некоторого числа m различных классов изображений или образов в n-мерном пространстве задаются в виде точек . Любое входное изображение Si также представляется в виде точки  в этом пространстве. Принадлежность входного изображения Sk к одному из m классов определяется с помощью расстояний между точкой Si и всеми точками X1, X2,…, Xm, соответствующими эталонным образцам. Расстояние и является мерой сходства входного изображения с эталонами классов или образов. Входное изображение относится к тому образу, расстояние до эталонного изображения которого минимально, т.е. решающим правилом является следующее соотношение:
                                .                            (1)
В теории распознавания образов часто используются расстояния по Евклиду (2) и по Минковскому (3):
                                         ;                                          (2)
                                         .                                          (3)
где   – целое положительное число, большее двух.
Операции возведения в степень и извлечения корня не всегда удобно использовать при определении расстояний, поскольку они являются нелинейными операциями. Поэтому для определения расстояний в пространстве изображений часто используется и сумма модулей разностей между соответствующими компонентами n-мерных векторов:
                                                 .                                         (4)
В выражения (2) – (4) разности всех компонентов векторов входят с одинаковыми единичными весами. В тех случаях, когда компоненты векторов, соответствующих распознаваемым изображениям, отличаются на порядки, например, одни компоненты векторов измеряются метрами, а другие – сантиметрами или миллиметрами, то при использовании расстояний (2) – (4) компоненты, имеющие небольшие численные значения, могут практически не влиять на величину расстояний. В то же время с точки зрения решения реальных задач распознавания именно эти компоненты могут играть определяющую роль. Поэтому для более адекватного учета подобных компонент  в выражения (2) – (4) могут вводиться весовые коэффициенты, учитывающие практическую ценность различных компонент вектора. В этом случае выражения (2) – (4) преобразуются к виду:
                                     ;                                          (5)
                                     .                                          (6)
                                         .                                             (7)
Предварительное задание весовых коэффициентов в формулах, определяющих расстояния, требует наличия определенной априорной информации и не всегда может быть сделано оптимальным образом. Поэтому особый интерес представляют расстояния, в которых заложена идея выравнивания весов слагаемых от различных компонент, если они существенно отличаются по своим абсолютным значениям. Примером такого расстояния является расстояние по Камберру:
                                             .                                            (8)
При решении задач распознавания сигналов часто возникают ситуации, когда сигналы, отличающиеся только амплитудой или смещением по оси ординат, или небольшими нелинейными искажениями, необходимо относить к одному классу. В этом случае может использоваться расстояние по Кендалу:
                                     ,                                 (9)
где 

Если компоненты обоих векторов Si и Xj упорядочены однотипно, то , и результат суммирования в выражении (9) равен половине числа размещений из n по два: . Отсюда следует, что выражение (9) при однотипном упорядочении векторов Si и Xj принимает минимальное значение, равное нулю:
.
Если  ни при одном значении индексов q и k, то любое произведение , и, следовательно, в этом случае . Таким образом, расстояние по Кендалу может принимать значения из интервала [0, 2]. Расстояние по Кендалу – это и расстояние для оценки близости в некотором смысле двух функций, заданных в n точках. Для оценки близости двух функций F(x) и G(x), заданных векторами своих значений в n точках, часто применяется и расстояние по Чебышеву:
                                  .                                  (10)

## 3. Индивидуальные задания
3.1. Разработайте алгоритм и программу, моделирующую распознавание различных объектов в n-мерном векторном пространстве с помощью расстояний (2) – (10).
3.2. Задайтесь размерностью n-мерного векторного пространства и числом m эталонных объектов образов (n и m должны быть не менее 5). Задайтесь несколькими объектами и с помощью выражений (2) – (8) определите их принадлежность к тому или иному образу. 
3.3. Предложите свои примеры, иллюстрирующие недостатки расстояний (2) – (4) по сравнению с расстояниями (5) – (7).
3.4. Предложите не менее трех своих примеров распознавания с помощью расстояния по Кендалу. По крайней мере в одном из примеров расстояние по Кендалу должно принимать минимальное значение, а в другом – максимальное.
3.5. Предложите несколько примеров распознавания с помощью расстояния по Чебышеву. В одном из примеров расстояние по Чебышеву должно принимать значение, равное Вашему номеру по списку в журнале группы. 
3.6. Предложите пример распознавания, в котором величины расстояний по Чебышеву и Кендалу будут равны.

## 4. Содержание отчета
4.1. Тема лабораторного занятия.
4.2. Индивидуальное задание.
4.3. Результаты выполнения пунктов 3.1 – 3.6 индивидуального задания.
