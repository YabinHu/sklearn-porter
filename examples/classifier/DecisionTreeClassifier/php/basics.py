from sklearn.tree import tree
from sklearn.datasets import load_iris

from sklearn_porter import Porter

X, y = load_iris(return_X_y=True)
clf = tree.DecisionTreeClassifier()
clf.fit(X, y)

# Cheese!

result = Porter(language='php').port(clf)
print(result)

"""
<?php

class Tmp {

    public static function predict($atts) {
        if (sizeof($atts) != 4) { return -1; }

        $classes = array_fill(0, 3, 0);

        if ($atts[3] <= 0.80000001192092896) {
            $classes[0] = 50;
            $classes[1] = 0;
            $classes[2] = 0;
        } else {
            if ($atts[3] <= 1.75) {
                if ($atts[2] <= 4.9499998092651367) {
                    if ($atts[3] <= 1.6500000953674316) {
                        $classes[0] = 0;
                        $classes[1] = 47;
                        $classes[2] = 0;
                    } else {
                        $classes[0] = 0;
                        $classes[1] = 0;
                        $classes[2] = 1;
                    }
                } else {
                    if ($atts[3] <= 1.5499999523162842) {
                        $classes[0] = 0;
                        $classes[1] = 0;
                        $classes[2] = 3;
                    } else {
                        if ($atts[0] <= 6.9499998092651367) {
                            $classes[0] = 0;
                            $classes[1] = 2;
                            $classes[2] = 0;
                        } else {
                            $classes[0] = 0;
                            $classes[1] = 0;
                            $classes[2] = 1;
                        }
                    }
                }
            } else {
                if ($atts[2] <= 4.8500003814697266) {
                    if ($atts[1] <= 3.0999999046325684) {
                        $classes[0] = 0;
                        $classes[1] = 0;
                        $classes[2] = 2;
                    } else {
                        $classes[0] = 0;
                        $classes[1] = 1;
                        $classes[2] = 0;
                    }
                } else {
                    $classes[0] = 0;
                    $classes[1] = 0;
                    $classes[2] = 43;
                }
            }
        }

        $class_idx = 0;
        $class_val = $classes[0];

        for ($i = 1; $i < 3; $i++) {
            if ($classes[$i] > $class_val) {
                $class_idx = $i;
                $class_val = $classes[$i];
            }
        }
        return $class_idx;
    }

}

if ($argc > 1) {
    array_shift($argv);
    $prediction = Tmp::predict($argv);
    fwrite(STDOUT, $prediction);
}
"""
