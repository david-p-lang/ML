
import Cocoa
import CreateML


var trainData = try MLDataTable(contentsOf: URL(fileURLWithPath: "/Users/davidlang/Desktop/all/train.csv"))
let testData = try MLDataTable(contentsOf: URL(fileURLWithPath:"/Users/davidlang/Desktop/all/test.csv"))
trainData = trainData.dropMissing()

let paramters = MLLogisticRegressionClassifier.ModelParameters(validationData: trainData,
                                                               maxIterations: 100,
                                                               l1Penalty: 8.0,
                                                               l2Penalty: 0.0,
                                                               stepSize: 4.0,
                                                               convergenceThreshold: 0.01,
                                                               featureRescaling: true)

let model = try MLLogisticRegressionClassifier(trainingData: trainData, targetColumn: "Survived", featureColumns: nil, parameters: paramters)

let metrics = model.validationMetrics
let evaluation = model.evaluation(on: testData)

print(metrics)
print(evaluation.precisionRecall)

let id = testData["PassengerId"]

for i in 0...id.count - 1 {
    print("\(id[i].intValue!) \(try model.predictions(from: testData)[i].intValue!)")
}
