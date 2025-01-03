# Nym Assignment

## Introduction

Welcome to the Nym Software Engineer Home Assignment! Thank you for taking the time to work on this task. In this assignment, you will demonstrate your ability to work with external libraries and your understanding of software implementation by parsing and processing PDF documents.

As a Software Engineer in the Implementation team at Nym, your main task will be learning new components and plugins, and implementing them efficiently. This exercise simulates a common task that the team performs when onboarding a new client — parsing PDF documents.

## Task Overview

In this assignment, you will create a Python package named `nym_assignment` and implement functions for parsing PDF documents using the `pdfplumber` library.

The key deliverables are:

1. Implementing the `pdf_to_dict` function to parse the contents of a PDF into a dictionary of pages.
2. Populating the `Chart` object with patient information, including Name, Date of Birth (DOB), and whether EKG results are valid.
3. Implementing the `pdf_to_extra_dict` function to extract additional attributes (e.g., fontname, size) from the PDF.

## Installation

Before running the assignment, make sure you have the required dependencies installed. You can install the necessary libraries using `pip`:

```bash
pip install pdfplumber
