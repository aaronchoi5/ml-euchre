
# Overall Test Plan

We will use _(insert test framework here)_ to make sure that the functionality that is used by the UI works as expected.

## Test Case Descriptions

### 1. Deal phase starts the round correctly

**Purpose:** To make sure that the program starts the hand correctly.

**Description:** This will run the deal functionality that starts each hand and make sure that it sets the game up successfully.

**Input:** Possible outcomes

**Expected Output:** Each player has 5 cards, the kitty exists, and a card is turned up.

_normal_ / _blackbox_ / _functional_ / _integration_

### 2. Correctly record the data for each trick

**Purpose:** To verify that data is being recorded in such a way that can be used for decision modeling.

**Description:** We will both manually check the data based on the logical flow and what we know about the game and automatically check that the necessary fields are being captured.

**Input:** Program variables, logical components

**Expected Output:** Structured data with trick information

_normal_ / _blackbox_ / _functional_ / _integration_

### 3. Correctly record the data for each round

**Purpose:** To verify that data is being recorded in such a way that can be used for decision modeling.

**Description:** We will both manually check the data based on the logical flow and what we know about the game and automatically check that the necessary fields are being captured.

**Input:** Program variables, logical components

**Expected Output:** Structured data with round information

_normal_ / _blackbox_ / _functional_ / _integration_

### 4. Correctly record the data for each game

**Purpose:** To verify that data is being recorded in such a way that can be used for decision modeling.

**Description:** We will both manually check the data based on the logical flow and what we know about the game and automatically check that the necessary fields are being captured.

**Input:** Program variables, logical components

**Expected Output:** Structured data with game information

_normal_ / _blackbox_ / _functional_ / _integration_

### 5. Output a CSV with play data

**Purpose:** To have the data in a format that can be easily used, manipulated, verified, etc.

**Description:** We will use a python package along with the structured data collected from tricks, rounds, and games to compile a CSV file that will be exported at the end of gameplay simulation.

**Input:** Structured data

**Expected Output:** CSV file containing structured data

_normal_ / _blackbox_ / _functional_ / _integration_

### 6. Allow a user to play and interact with 3 AI players

**Purpose:** To allow the model to play against human players for the purposes of practicing gameplay.

**Description:** We will give the user an interface to interact with that will display their hand, what's been dealt, trick status, etc. that will allow them to play as they normally would with a deck of cards and three other plays.

**Input:** User input

**Expected Output:** Interactive gameplay

_normal_ / _whitebox_ / _functional_ / _integration_

### 7. Test basic heuristics of Euchre gameplay

**Purpose:** To gauge whether or not the desision modeling is accurately abiding by basic Euchre gameplay standards.

**Description:** We will create a set of unit tests representing basic Euchre gameplay standards. If certain scenarios are encountered, we will test if the model chose the correct move and what percentage of the time it does.

**Input:** Unit tests, trick data

**Expected Output:** Unit test results

_normal_ / _blackbox_ / _performance_ / _unit_

### 8. Test advanced heuristics of Euchre gameplay

**Purpose:** To gauge whether or not the desision modeling is accurately abiding by advanced Euchre gameplay standards.

**Description:** We will create a set of unit tests representing advanced Euchre gameplay standards. If complex scenarios are encountered that hold certain significance, we will test if the model decided moves correctly and what percentage of the time it does.

**Input:** Unit tests, trick data

**Expected Output:** Unit test results

_abnormal_ / _blackbox_ / _performance_ / _unit_

### 9. Integrate data generation into the learning model

**Purpose:** To allow continuous self-play and learning; constant flow of data collection and improvement.

**Description:** We will marry the standard Euchre gameplay ruleset with the reinforcement model built off of the data that we generated, so that it is a continuous loop of input, output, and improvement.

**Input:** Gameplay framework, initial ruleset, reinforcement learning model.

**Expected Output:** A continuous model that generates data and improves decision making.

_abnormal_ / _whitebox_ / _functional_ / _integration_

## Test Coverage

| ID | Norm / Ab / Edge | Black / White Box | Func. / Perf. | Unit / Int. |
| -- | ---------------- | ----------------- | ------------- | ----------- |
| 1  | Normal           | Blackbox          | Functional    | Integration |
| 2  | Normal           | Blackbox          | Functional    | Integration |
| 3  | Normal           | Blackbox          | Functional    | Integration |
| 4  | Normal           | Blackbox          | Functional    | Integration |
| 5  | Normal           | Blackbox          | Functional    | Integration |
| 6  | Normal           | Whitebox          | Functional    | Integration |
| 7  | Normal           | Blackbox          | Performance   | Unit        |
| 8  | Abnormal         | Blackbox          | Performance   | Unit        |
| 9  | Abnormal         | Whitebox          | Functional    | Integration |