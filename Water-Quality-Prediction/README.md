# Final Portfolio Piece (Project) Idea – Water Quality Prediction

**What are you doing? What is the question?**

The United States has one of the safest water supplies in the world. Over 90 percent of Americans get their tap water from community water systems, which are subject to safe drinking water standards.

Still As many as 63 million people — nearly a fifth of the United States — from rural central California to the boroughs of New York City, were exposed to potentially unsafe water more than once during the past decade, according to a News21 investigation of 680,000 water quality and monitoring violations from the Environmental Protection Agency.

The findings highlight how six decades of industrial dumping, farming pollution, and water plant and distribution pipe deterioration have taken a toll on local water systems.

Of six environmental problems facing the U.S., Americans remain most worried about those that affect water quality. Majorities express "a great deal" of worry about the pollution of both drinking water (56%) and rivers, lakes and reservoirs (53%).

Drinking water quality varies from place to place, depending on the condition of the source water from which it is drawn and the treatment it receives, but it must meet U.S. Environmental Protection Agency (EPA) regulations. Community water systems follow the rules set forth by the Safe Drinking Water Act (SDWA).external icon (Links to an external site.) Many states enforce their own drinking water standards that are at least as protective as EPA’s national standards. The SDWA rules include guidelines for drinking water quality, water testing schedules, and water testing methods.

The presence of certain contaminants in our water can lead to health issues, including gastrointestinal illness, reproductive problems, and neurological disorders. Infants, young children, pregnant women, the elderly, and people with weakened immune systems (Links to an external site.) may be especially at risk for illness.

 **Data? Where is the data?**

In this Dataset we will be primarily focusing on the:
·       Groundwater:
.Nearly 40 percent of Americans (Links to an external site.) rely on groundwater, pumped to the earth’s surface, for drinking water. For some folks in rural areas, it’s their only freshwater source. Groundwater gets polluted when contaminants—from pesticides and fertilizers to waste leached from landfills and septic systems
·       Surface water
Surface water from freshwater sources (that is, from sources other than the ocean) accounts for more than 60 percent (Links to an external site.) of the water delivered to American homes. But a significant pool of that water is in peril. They have become a major pollutant (Links to an external site.) due to farm waste and fertilizer runoff junk that industry and individuals dump directly into waterways.

We will be testing the potability of water from three of the topmost water polluted states in the USA:
1.       Texas
2.       Pennsylvania
3.       Florida
 

**Features:**

1) **ph** : Indicator of acidic or alkaline condition of water, ranging from 1 to 14.
Acceptable Limit: 6.5 to 8.5

2) **Hardness** : Capacity of water to precipitate soap in mg/L.
Acceptable Limit: Upto 500 or 600 mg/L

3) **Solids** : Total dissolved solids (TDS) in ppm. The water with high TDS value indicates that water is highly mineralized.
Acceptable Limit: 500 - 1000 ppm

4) **Sulfate** : Amount of Sulfates dissolved in water in mg/L.
Acceptable Limit: Upto 400 mg/L

5) **Conductivity** : Electrical conductivity of water in μS/cm.
Acceptable Limit: Upto 400 μS/cm

6) **Organic_carbon** : Amount of carbon in organic compounds in ppm.
Acceptable Limit: Less than 2 mg/L

7) **Trihalomethanes**: Amount of Trihalomethanes in μg/L.
Acceptable Limit: Upto 80 ppm

8) **Turbidity**: Measure of light emiting property of water in NTU.
Acceptable Limit: 5-10 NTU

9) **Potability**: Indicates if water is safe for human consumption.
Here Potable -1 and Not potable -0.

 

**Datasets:**

https://www.kaggle.com/adityakadiwal/water-potability (Links to an external site.)

https://waterdata.usgs.gov/nwis/annual/?referred_module=qw (Links to an external site.)

 

**Which Algorithms? What approaches?**

1) Logistic Regression Training Accuracy: LogisticRegression(random_state=101)
2) SVC Training Accuracy: SVC(random_state=101)
3) Decision Tree Training Accuracy: DecisionTreeClassifier(criterion='entropy', random_state=101)
4) Random Forest Training Accuracy: RandomForestClassifier(criterion='entropy', n_estimators=10, random_state=101)
5) NN Training Accuracy: KNeighborsClassifier(n_neighbors=3)
6) GradiendBoosting Training Accuracy: GradientBoostingClassifier(random_state=101)
7) AdaBoosting Training Accuracy: AdaBoostClassifier(random_state=101)
8) XGBoosting Training Accuracy: XGBClassifier(base_score=0.5, booster='gbtree', class_weight=None

**Objective:**
We will try to predict the relationship between all the features:

In this Dataset, we have a binary classification problem.
We will make a prediction on the target variable Potability
Lastly, we will build a variety of models and try to define the model giving the best prediction on potability.
 

**Evaluation? How do you know it worked?**
We will be evaluating by following the below steps:

1) Data Preparation
2) Model Training
3) Model Optimization
4) Model Evaluation:

After all Machine learning steps are completed and all the algorithms and models are executed, we will compare the accuracy and Rank the Algorithms based on their accuracy.

**References:**

https://www.cdc.gov/healthywater/drinking/public/water_quality.html (Links to an external site.)

https://www.multipure.com/purely-social/science/top-10-states-worst-public-water-ratings-united-states/ (Links to an external site.)

https://news.gallup.com/poll/347735/water-pollution-remains-top-environmental-concern.aspx (Links to an external site.)

https://www.nrdc.org/stories/water-pollution-everything-you-need-know (Links to an external site.)

https://www.usatoday.com/story/news/2017/08/14/63-million-americans-exposed-unsafe-drinking-water/564278001/ (Links to an external site.)

https://www.kaggle.com/neesha12/water-potability-analysis/notebook (Links to an external site.)

 
