# Summary of early findings (draft)

 
## Overview

171 studies have been reviewed that cited the original STRESS guideline in their reference lists using Google Scholar. After removing duplicates, 165 unique studies were identified. Of these, 73 studies explicitly claimed to have used the guideline to report their simulation studies. However, only 45 of these studies applied all elements of the guideline. In the remaining 28 studies, certain elements were either partially applied or omitted. For instance, while most studies reported elements such as "objective" and "logic," many did not fully address "implementation" or "code access," with some only mentioning parts of the implementation process.

Of all the studies that used the STRESS guideline, 14 were authored or co-authored by at least one of the original guideline's developers. The fact that 14 studies involving the original authors adhered to the guideline suggests that the creators of STRESS are actively contributing to the body of research and applying their own framework. 

In terms of journal distribution, the dataset revealed that papers were published across various journals, primarily focusing on areas related to the healthcare domain (this is further highlighted and discussed in RQ5 and Fig 4). Notable journals included Healthcare Management Science, BMJ, Health Systems, and Health and Social Care Delivery Research. However, the Journal of Simulation was the most frequently cited journal among the studies that employed the STRESS guideline, with 11 papers published in this journal. Following closely was the Winter Simulation Conference, which featured six papers utilizing STRESS.


## Research Questions
#### 1. How many references are using STRESS to document their model versus general citation and discussion (how else has STRESS been used).

73 studies claimed to use the STRESS guideline to report their simulation work. This could be further break down to:

Full Use of the STRESS Guideline: 45 studies used all elements of the guideline.
Partial Use of the STRESS Guideline: 28 studies applied only some elements.

From the 165 unique studies, subtracting the 73 that claimed to use the guideline leaves 92 studies that cited STRESS in a more general way, without directly using it to document their own models. Some papers cited STRESS to compare it with other simulation reporting framework such as the study by Pawel et al. (2022) and Moallemi et al. (2020). Researchers used STRESS to critique or discuss existing methodologies, offering insights into its strengths or limitations. Furthermore, in a study conducted by Howick et al. (2024), authors offer insights for extending the STRESS to encompass hybrid simulation, with a focus on SD and ABS hybridisation. Moreover, there were 17 literature reviews in the dataset (out of 165 papers), highlighting the guideline being recognised as a key framework in broader discussions within the academic community. Moreover, in a study by Nwanosike (2023), they used the STRESS checklist for assessing the quality of the simulation studies. 

#### 2. How has the used in terms of documenting models changed over time.
Fig 3. Examining the studies that used STRESS over time reveals a notable increase in its adoption since its publication in 2019. The highest usage occurred in 2022, with 18 papers out of 73 employing the guideline, followed by 17 papers in both 2021 and 2023. This upward trend demonstrates growing recognition and acceptance of the STRESS guideline within the academic community. This rise may be attributed to the increasing use of simulation studies, where clear reporting standards become essential for transparency and reproducibility. It also highlights the importance of continuing to update and refine the guideline to ensure it meets the evolving needs of simulation researchers.



#### 3. What is the breakdown of the literature that used STRESS for DES, SD and ABS
Fig 2. In terms of simulation methods, DES was the most commonly used, appearing in 38 papers, followed by ABS in 14 papers. Additionally, seven studies employed hybrid simulation approaches, underscoring the need to extend the guideline to better accommodate the reporting of hybrid simulations. There were also five SD models which used the guideline.
Additionally, while the original STRESS guideline did not specifically address reporting for Monte Carlo simulations, six studies employing Monte Carlo simulation have nonetheless utilised the STRESS guideline. Notably, one of these studies found that STRESS-DES was more closely aligned with the principles of Monte Carlo simulation (study no 63, Denz et al., 2023).


#### 4. Has STRESS been used to document any hybrid simulation models? If so how has it been used (e.g. multiple checklists); have modifications been introduced have alterantive guidelines been used?
Yes, STRESS has been utilized to document hybrid simulation models, as evidenced by the seven studies that employed hybrid simulation approaches while referencing the guideline.
- Three DES+ABS, 
- Two SD+ABS, 
- One ABS+SD+DES
- and, one Monte Carlo + machine learning
Researchers may have integrated elements from both STRESS and other relevant guidelines to comprehensively report their hybrid models such as the study by Allen et al. (2020) which used TRIPOD protocol for reporting machine learning and STRESS for Monte Carlo.
Some of these studies have adapted the STRESS guideline to better fit the unique requirements of hybrid simulations, potentially introducing modifications or additional reporting elements tailored to the complexities of these models. For example, in the SD+ABS model of Shukla et al (2022), they employed the guideline in a structured way in the paper's main text, although not all aspects of their ABS model has been reported (while most of the elements have been reported for SD, only the logic element has been described for ABS). 


#### 5. What are the fields of application where STRESS has been used? (e.g. manufacturing, healthcare etc)
Fig 4. In terms of application areas, the STRESS guideline has been predominantly applied in healthcare, with 56 out of 73 studies falling within this domain. These studies encompassed various case studies and operational research problems, including staffing, patient flow, disease transmission, and disease diagnosis. The second application area, after healthcare, is supply chain and operations, which includes sectors such as the food industry, drug industry, mining operations, and supply chain financing. Additionally, a few studies addressed other application areas, including hospitality and tourism, water resource management, business analytics, and geography and environmental science.

#### 6. How did authors use STRESS to document their models.
Checklist supplement pointing to paras, lines etc?
Sections within the main paper or appendix?
Something else?
Fig 6. The authors of papers utilising the STRESS guideline were classified based on how they documented their models into three categories: checklist, structured, and unstructured formats.

A. Checklist Format:
This format was employed in 19 papers, primarily located in the appendix rather than the main text. Most of these papers utilised the same checklist provided in the original STRESS guideline.

B. Structured Format:
A structured format was identified in 32 papers, where authors provided detailed descriptions referencing all or some of the STRESS elements. This format was predominantly found in the main text, with 26 papers incorporating it there and 6 using it in the appendix.

C. Unstructured Format:
The unstructured format was present in 19 papers, where authors mentioned the STRESS elements in a less organised manner. Of these, seven papers included references to the elements in the main text, while 12 did so in the appendix. Locating the STRESS elements in these papers often required additional time and effort due to the lack of systematic organisation.This challenge may hinder reproducibility and transparency of simualtion studies.

The prevalence of the checklist format, particularly in the appendix, suggests that researchers value the straightforwardness of this method but may not prioritise its visibility in the main text, possibly due to word count limitations.

#### 7. Are there any sections of STRESS that caused authors problems?
Certain elements of the STRESS guideline, particularly those related to implementation—such as model execution and random sampling—were mentioned less explicitly and less frequently compared to other elements. However, authors did not provide specific reasons for these omissions; many simply neglected to include certain components without justification.

Regarding the objective element, the aims of the experiments were discussed less frequently across the simulation studies. Similarly, the algorithms and model components within the logic elements received limited reporting, indicating a general lack of emphasis on these foundational aspects.

In terms of the data element, while authors predominantly covered data sources and input parameters, assumptions and preprocessing steps were among the most overlooked aspects in simulation reporting. Additionally, the estimation approach outlined in the experimentation elements garnered limited attention from authors.

Finally, the code access element was referenced in 38 studies that employed the STRESS guideline. A further assessment of the papers that provided a code access statement revealed that most authors shared their source code through links to repositories such as GitHub or included it as an appendix (23 papers). Eleven studies indicated that the code would be available upon request, while a few papers mentioned confidentiality reasons for not sharing the model or stated that they would provide it in future publications.


#### 8. How has each section of STRESS been used? Do any need to be clarified or rephrased?
Refer to answer for question no 7.

#### 9. Are additional sections or modifications to sections needed to improve model reporting (unclear if a review will answer this question.)
- One study has mentioned to the need for validation and verification section (Achter et al., 2022).
- Given the increasing prevalence of hybrid simulations combining various methodologies, there may be a need for dedicated sections addressing the unique reporting requirements for these models. This could include guidelines on integrating different methods and presenting their interactions.
- Adding/ introducing some papers outlining good practices could improve the use of the guideline, particularly, the sections that are under represented in the reports such as those that mentioned in question no 7. 


#### 10. What modifications are needed to document a hybrid model?
- The aim/ reason for hybridisation.
- The specific components and interactions between them.
- The data exchange method between the models, interaction rules, and synchronisation.



### Notes
- Study No. 25: Wood et al., 2020: The STRESS study was fully used but not cited - however, it showed up in the cited results!
- Study No. 43 provides valuable insights for extending the guideline to incorporate hybrid simulation approaches, particularly a conceptual framework for hybrid Agent-Based Modeling and System Dynamics (ABM+SD) models.
- Study No. 51: Gadomski et al. (2021): The authors claim to have used the guideline, but there is no evidence supporting this claim.
- Study No. 64: Conlon & Molloy (2023): This study refers to supplementary material for the guideline; however, I could not find the mentioned supplementary section or file.
- Study No. 113: Saville et al. (2022): The authors did not claimed the use of STRESS but there are some elements of the guideline (it might be due to the fact that the simulation is not the focus of the study instead the classification is)
- Study No. 115: Birchansky et al. (2021): I doubt that they used STRESS. Except for the name, no elements has been mentioned altough some concepts of the elements are included.
- Study No. 138: Stokes (2020): Reassessment needed! Although the author claims to have used the guideline, I was unable to locate the elements within the text.
- Study No. 161: Hajlasz (2023): This thesis is not in English, so analysis has not been conducted. However, it appears that the author may have used the guideline. Further language support is needed for assessment.