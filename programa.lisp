(defun zero (x);funcion cero con parametro de entrada
(+ 0 0)
)

(defun cero ();funcion cero sin parametro de entrada
(+ 0 0)
)

(defun suce(a);funcion sucesor
(+ a 1)
)

;funcion proyeccion, primer parametro es el elemento con index de 1 y el segundo la lista, entrada como '()
(defun proj (m n)
    (nth (- m 1) n)
)

(defun suma (x y)
    (if (= y 0)
        (proj 1 (list x))
        (suce (proj 3 (list x (- y 1) (suma x (- y 1)))))
    )
)


(defun mult (x y)
    (if (= y 0)
        (proj 1 (list 0))
        (suma x (mult x (- y 1)))
    )
)

(defun expo (x y)
    (if (= y 0)
        (proj 1 (list 1))
        (mult x (expo x (- y 1)))
    )
)

(defun pred (y)
    (if (= y 0)
        (cero )
        (proj 1 (list (- y 1) (pred (- y 1))))
    )
)

(defun monus (x y)
    (if (= y 0)
        (proj 1 (list x))
        (pred (monus x (- y 1)))
    )
)

(defun equ (x y)
    (monus 1 (suma (monus y x) (monus x y)))
)


(defun coci (x y)
    (if (or (zerop y) (zerop x))
        (proj 1 (list 0))
        (suma (coci (- x 1) y) (equ x (suma y (mult (coci (- x 1) y) y))))
    )
)


(defun fib (x)
    (if (= x 1)
        (+ 0 0)
        (if (= x 2)
            (+ 1 0)
            (if (> x 2)
                (suma (fib (- x 1)) (fib (- x 2)))
            )
        )
    )
)

(defun impa (x)
    (if (= x 0)
        (proj 1 (list 0))
        (monus x (mult 2 (coci x 2)))
    )
)

(defun fact (x)
    (if (= x 0)
        (proj 1 (list 1))
        (mult x (fact (- x 1)))
    )
)

(defun div (x y)
    (setq g 10)
    (setq a 0)
    (loop
            (setq g (monus (suma x 1)  (suma (mult a y) y ) ))
            (when (= g 0) (return a))
            (setq a (suce a))
    )
)

(defun A (x y)
    (if (= x 0)
        (+ y 1)
        (if (and (> x 0) (zerop y))
            (A (- x 1) 1)
            (if (and (> x 0) (> y 0))
                (A (- x 1) (A x (- y 1)))
            )
        )
    )

)



(write (div 8 3))
