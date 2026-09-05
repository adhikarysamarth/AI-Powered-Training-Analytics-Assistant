# AI-Powered Training Analytics Assistant

## Data Dictionary

### Dataset Overview

This dataset contains student inquiry, enrollment, training, completion, funding, and employment placement information collected by a training institution.

The dataset is used to support:

- Enrollment analytics
- Training performance analysis
- Student completion tracking
- Placement outcome reporting
- Funding source reporting
- AI-powered natural language analytics

---

## Data Fields

### Course Package
**Data Type:** String

Name of the training package or course selected by the student.

**Example:** SQL Developer, Full Stack Web Development, AI Fundamentals

---

### Academic Year
**Data Type:** Integer

Academic year in which the student was enrolled.

**Example:** 2025

---

### Inquiry Date
**Data Type:** Date

Date when the student first contacted the institution for information.

**Example:** 2025-01-15

---

### Registration No
**Data Type:** String

Unique student registration number assigned by the school.

**Example:** 900123456

---

### Admission Batch
**Data Type:** String

Month or enrollment batch of the student.

**Example:** January 2025

---

### Training Program Funding Source
**Data Type:** String

Organization or funding source responsible for paying training costs.

**Examples:**

- WIOA
- Trade
- Section 30
- Self Pay

---

### Start Date
**Data Type:** Date

Date the training program begins.

**Example:** 2025-03-01

---

### Expected End Date
**Data Type:** Date

Expected completion date for the training program.

**Example:** 2025-08-30

---

### Admission Date
**Data Type:** Date

Official date the student enrolled in the program.

**Example:** 2025-02-20

---

### Student Name
**Data Type:** String

Full name of the student.

**Example:** John Smith

---

### Lead Source
**Data Type:** String

Source from which the student inquiry originated.

**Examples:**

- Career Center
- Phone Call
- Email
- Referral

---

### Counselor
**Data Type:** String

School counselor responsible for student admission.

**Example:** Jane Doe

---

### Counselor Email
**Data Type:** String

Email address of the counselor.

**Example:** counselor@school.edu

---

### Gender
**Data Type:** String

Student gender.

**Examples:**

- Male
- Female
- Other

---

### Admission Status
**Data Type:** String

Current training status of the student.

**Examples:**

- Training Completed
- In Training
- Dropped Out
- Incomplete

---

### State
**Data Type:** String

State associated with the student or funding source.

**Examples:**

- MA
- NH
- NY
- FL

---

### Lead Stage
**Data Type:** String

Current stage within the student lifecycle.

**Examples:**

- New Inquiry
- Admitted
- Did Not Join
- Training Completed
- Dropped Out

---

### Package Amount
**Data Type:** Decimal

Tuition or training cost for the selected program.

**Example:** 8500.00

---

### Placement Salary Range
**Data Type:** String

Salary range associated with student employment placement.

**Example:** $50,000 - $75,000

---

### Placement Job Title
**Data Type:** String

Job title obtained after completing training.

**Example:** SQL Developer

---

### Placement Information
**Data Type:** Boolean

Indicates whether the student obtained employment placement.

**Allowed Values:**

- Yes
- No

---

### Placement Employer
**Data Type:** String

Name of the employer where the student was placed.

**Example:** Microsoft

---

### Placement Remark
**Data Type:** String

Additional notes regarding placement activities.

---

### Assigned Career Center
**Data Type:** String

Career center responsible for referring or supporting the student.

**Example:** Boston Career Center

---

## Derived Analytics Fields

The following fields will be created during data cleaning and transformation.

### Enrollment Year
**Data Type:** Integer

Year extracted from Admission Date.

---

### Enrollment Month
**Data Type:** String

Month extracted from Admission Date.

---

### Inquiry To Admission Days
**Data Type:** Integer

Number of days between Inquiry Date and Admission Date.

---

### Training Duration Days
**Data Type:** Integer

Number of days between Start Date and Expected End Date.

---

### Completed
**Data Type:** Integer

Completion indicator.

**Values:**

- 1 = Training Completed
- 0 = Not Completed

---

### Placed
**Data Type:** Integer

Placement indicator.

**Values:**

- 1 = Placed
- 0 = Not Placed

---

## Data Quality Rules

1. Registration No must be unique.
2. Registration No cannot be null.
3. Admission Date should be on or after Inquiry Date.
4. Expected End Date should be after Start Date.
5. Package Amount cannot be negative.
6. State values should use standardized abbreviations.
7. Placement Information should contain only Yes or No.
8. Admission Status should use approved status values.

