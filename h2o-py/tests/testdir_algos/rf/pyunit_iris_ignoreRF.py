import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils




def iris_ignore():



  iris = h2o.import_file(path=pyunit_utils.locate("smalldata/iris/iris2.csv"))

  from h2o.estimators.random_forest import H2ORandomForestEstimator

  for maxx in range(4):
    model = H2ORandomForestEstimator(ntrees=50, max_depth=100)
    model.train(y=4, x=range(maxx+1), training_frame=iris)
    model.show()




if __name__ == "__main__":
  pyunit_utils.standalone_test(iris_ignore)
else:
  iris_ignore()
