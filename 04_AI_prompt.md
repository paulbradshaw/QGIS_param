# Using AI to adapt Python code for QGIS

When using AI it's important to assess a number of common risks*, identify what steps can be taken to manage those, and then decide whether it is worth it.

Deskilling is one of the risks to assess. One step to manage that is to [use roleplay prompting](https://onlinejournalismblog.com/2025/11/28/4-ways-you-can-role-play-with-ai/) to give the AI the role of a mentor who doesn't want to deskill you.

Here is a template prompt to do that:

```
You are my mentor, a data journalist with over a decade's experience in the field. You have advanced statistical knowledge as well as a healthy scepticism when dealing with both data and human sources. 
I will ask you for help with some coding - you are happy to guide me, but you don't want me to become deskilled and too reliant on you, so your advice will always be designed to force me to think for myself, learn new skills and concepts, and practise those.

When you provide code add comments explaining each step as if to a person with no coding experience. 
I prefer simple code that requires multiple lines to complex code in one or two lines.

Flag any assumptions you are making about the data or my question. Warn me if the question does not contain enough information to answer accurately, or if the result could be misleading without additional context.
```

For the QGIS code, you can then either add the next part at the bottom, or in a subsequent prompt, attaching [the Python script used earlier](https://github.com/paulbradshaw/QGIS_param/blob/main/qgis_take_pix.py) in the workshop:

```
Attached is some Python that generates images for maps centred at hundreds of locations. Adapt this so that it now generates those images at two different scales.

Comment the code to highlight the section of code where it does this, so that I can tweak it and try different zoom levels.
```

You can also [use **meta prompting** to help design the prompt](https://github.com/paulbradshaw/QGIS_param/blob/main/ai/vibecoding_gemini.md)

Other ways to address deskilling include [parallel prompting](https://onlinejournalismblog.com/2026/02/02/parallel-prompting-another-way-to-avoiding-deskilling-with-ai/) and [journey prompts](https://onlinejournalismblog.com/2025/12/02/journey-prompts-and-destination-prompts-how-to-avoid-becoming-deskilled-when-using-ai/) or [destination-journey prompting](https://onlinejournalismblog.com/2026/01/13/how-to-stop-ai-making-you-stupid-hybrid-destination-journey-prompting/)


*Other risks to assess include hallucination (accuracy), bias (including sycophancy and positivity bias), explainability, automation bias, and [environmental impact](https://onlinejournalismblog.com/2025/06/19/how-to-reduce-the-environmental-impact-of-using-ai/)
