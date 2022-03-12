# Random Module

## What is Random Module?
  - Is a predefined functions, used to generate random numbers.

## What functions that the Random Module Contain?
  1. **Randint**
     - Randint generates integer numbers, it accepts lowest and highest number
```
    print random.randint(0, 5)
    # output: either 1,2,3,4,or 5
``` 
  2. **Random**
     - Generate numbers between 0 and 1.
```
    print(random.random())
    # Output for Ex: 0.8071947810455896
``` 
  3. **Choice**
     -  Used to choice an element from a list randomly.
```
    myList = [2, 109, False, 10, "Lorem", 482, "Ipsum"]
    random.choice(myList)
    # Output for Ex: False
```
  4. **Shuffle**
     -  Shuffle used to reorder element in a list

```
    myList = [2, 109, False, 10, "Lorem", 482, "Ipsum"]
    random.shuffle(myList)
    print(myList)
    # Output for Ex: 482, 'Lorem', 2, 'Ipsum', False, 10, 109]
```

  5. **Randrange**
    - Generate randomly selected elements from range(start,stop,step)

```
    for i in range(3):
    print random.randrange(0, 101, 5)

    # Output for Ex:
            50
            40
            25
```

---

# Risk Analysis

## What is Risk Analysis?
  - Any unwanted inciden in applications are defined as **Risk**.
  - Risk Analysis is a process to identify the risks in an application and prioritizing them to tests.

## Why to use Risk Analysis?
  - If we use risk analysis at the beginning of a project, that will highlights the potential areas.
  - When risk areas become knowns, software developers can mitigate the risks.
  - When risk areas become knowns, we can add these risks to testing.
  - Example of risks to be encounter:
    - Use of new hardware.
    - Use of new technology.
    - Use of new automation tool.
    - The sequence of code.
    - Availability of test resources for the application.
  
  - There are some risks that are unavoidable:
    - The time that you allocated for testing.
    - A defect leakage due to the complexity or size of the application
    - Urgency from the clients to deliver the project.
    - Incomplete requirements.
  
  - In such cases, we have to tackle the situation with care. Following points can be taken care of:
    - Conduct Risk Assessment review meeting
    - Use maximum resources to work on high-risk areas
    - Create a Risk Assessment database for future use
    - Identify and notice the risk magnitude indicators: high, medium, low.

  * But what are **Risk Magnitude** ?
    * **High**: means the effect of the risk would be very high and non-tolerable. The company might face loss.
    * **Medium**: it is tolerable but not desirable. The company may suffer financially but there is a limited risk.

    * **Low**: it is tolerable. There lies little or no external exposure or no financial loss.

### Risk Identification
  - The sets of risks included in the risk identification process are:
    1. **Business Risks**: This risk come from the company.
    2. **Testing Risk**.
    3. **Premature Release Risk**.
    4. **Software Risks**.

### Risk Assessment
 ![Risk Assessment](./class-06-img/Risk%20Assessment.png)

### The perspective of Risk Assessment
  - There are three perspectives of Risk Assessment:

    - Effect
    - Cause
    - Likelihood

 --- 

# Test Coverage (Code coverage)
  
## What is test coverage?
  - Test coverage is a tool to finding untested parts of a codebase.
  - 

---

# Big-O
  - Big-O can be discribed as:
    - How code slows as data grows.
    - How much time the code will take, if the data are double, triple, or 10x times as what are exist.
  * Terminology O(N):
    * **N**: how much of data.
    * **O**: order of.
    * **O(1)**: constant time
    * **O(N)**: linear time.
    * **O(N^2)**: quadratic time.
---
## Resources
  1. [pythonforbeginners](https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python)
  2. [edureka](https://www.edureka.co/blog/risk-analysis-in-software-testing/#WhyuseRiskAnalysis?)
  3. [martinfowler](https://martinfowler.com/bliki/TestCoverage.html)
  4. [Youtube](https://www.youtube.com/watch?v=Ee0HzlnIYWQ)