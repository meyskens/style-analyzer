# Test report for javascript / file:///tmp/top-repos-quality-repos-irr0560m/webpack HEAD babe736cfa1ef7e8014ed32ba4a4ec38049dce14

### Classification report

PPCR: 0.971

| Class | Precision | Recall | Full Recall | F1-score | Full F1-score | Support | Full Support | PPCR |
|------:|:----------|:-------|:------------|:---------|:---------|:--------|:-------------|:-----|
| `∅` | 0.953| 0.987| 0.983| 0.970| 0.968| 39377| 39540| 0.996 |
| `␣` | 0.944| 0.976| 0.970| 0.960| 0.957| 17320| 17428| 0.994 |
| `⏎` | 0.886| 0.749| 0.657| 0.812| 0.754| 4846| 5529| 0.876 |
| `"` | 0.951| 0.969| 0.885| 0.960| 0.917| 3962| 4342| 0.912 |
| `⏎⇥⁺` | 0.969| 0.767| 0.748| 0.856| 0.845| 3183| 3261| 0.976 |
| `⏎⇥⁻` | 0.930| 0.827| 0.766| 0.876| 0.840| 2667| 2878| 0.927 |
| `␣"` | 0.904| 0.986| 0.831| 0.943| 0.866| 955| 1134| 0.842 |
| `⏎⏎` | 0.877| 0.608| 0.433| 0.718| 0.580| 857| 1204| 0.712 |
| `"⏎⇥⁻` | 0.918| 0.549| 0.539| 0.687| 0.679| 164| 167| 0.982 |
| `"␣` | 0.917| 0.804| 0.669| 0.857| 0.774| 138| 166| 0.831 |
| `⏎⇥⁻⇥⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 83| 86| 0.965 |
| `⏎"` | 0.825| 0.945| 0.945| 0.881| 0.881| 55| 55| 1.000 |
| `'` | 0.000| 0.000| 0.000| 0.000| 0.000| 29| 29| 1.000 |
| `␣'` | 0.000| 0.000| 0.000| 0.000| 0.000| 22| 22| 1.000 |
| `⏎⏎⇥⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 15| 17| 0.882 |
| `'␣` | 0.000| 0.000| 0.000| 0.000| 0.000| 10| 10| 1.000 |
| `⏎␣⁺␣⁺` | 0.000| 0.000| 0.000| 0.000| 0.000| 10| 10| 1.000 |
| `⏎␣⁻␣⁻` | 0.000| 0.000| 0.000| 0.000| 0.000| 10| 10| 1.000 |
| `macro avg` | 0.560| 0.509| 0.468| 0.529| 0.503| 73703| 75888| 0.971 |
| `weighted avg` | 0.942| 0.944| 0.917| 0.942| 0.926| 73703| 75888| 0.971 |
| `micro avg` | 0.944| 0.944| 0.917| 0.944| 0.931| 73703| 75888| 0.971 |

### Confusion matrix

|refusal|  ∅| ␣| ⏎| "| ⏎⇥⁺| ⏎⇥⁻| ␣"| ⏎⏎| '| "⏎⇥⁻| "␣| ⏎␣⁺␣⁺| ⏎␣⁻␣⁻| ␣'| ⏎⇥⁻⇥⁻| ⏎"| '␣| ⏎⏎⇥⁻| 
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|163 |38861 |449 |11 |0 |4 |50 |0 |0 |0 |0 |0 |2 |0 |0 |0 |0 |0 |0 |
|108 |210 |16910 |96 |0 |60 |44 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|683 |741 |353 |3631 |0 |0 |6 |52 |63 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|380 |17 |0 |0 |3841 |0 |8 |16 |0 |65 |4 |0 |0 |0 |0 |0 |11 |0 |0 |
|78 |486 |168 |7 |60 |2440 |0 |11 |0 |0 |0 |0 |11 |0 |0 |0 |0 |0 |0 |
|211 |342 |16 |95 |0 |0 |2205 |0 |9 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|179 |0 |0 |0 |11 |2 |0 |942 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|347 |90 |12 |234 |0 |0 |0 |0 |521 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |0 |29 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|3 |0 |0 |0 |74 |0 |0 |0 |0 |0 |90 |0 |0 |0 |0 |0 |0 |0 |0 |
|28 |0 |0 |0 |23 |0 |0 |0 |0 |0 |4 |111 |0 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |0 |0 |10 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |0 |0 |0 |10 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|0 |0 |0 |0 |0 |1 |0 |21 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|3 |26 |0 |12 |0 |0 |45 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |
|0 |0 |3 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |52 |0 |0 |
|0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |10 |0 |0 |0 |0 |0 |0 |0 |
|2 |0 |0 |12 |0 |0 |2 |0 |1 |0 |0 |0 |0 |0 |0 |0 |0 |0 |0 |

### Files with most errors

| filename | number of errors|
|:----:|:-----|

<details>
    <summary>Machine-readable report</summary>
```json
{
  "cl_report": {"\"": {"f1-score": 0.9602499999999999, "precision": 0.9512134720158494, "recall": 0.9694598687531549, "support": 3962}, "\"\u23ce\u21e5\u207b": {"f1-score": 0.6870229007633588, "precision": 0.9183673469387755, "recall": 0.5487804878048781, "support": 164}, "\"\u2423": {"f1-score": 0.8571428571428572, "precision": 0.9173553719008265, "recall": 0.8043478260869565, "support": 138}, "\u0027": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 29}, "\u0027\u2423": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 10}, "macro avg": {"f1-score": 0.5289206415390342, "precision": 0.5598064792372154, "recall": 0.5093450272808779, "support": 73703}, "micro avg": {"f1-score": 0.9443848961371993, "precision": 0.9443848961371993, "recall": 0.9443848961371993, "support": 73703}, "weighted avg": {"f1-score": 0.941692908651023, "precision": 0.9422891983302148, "recall": 0.9443848961371993, "support": 73703}, "\u2205": {"f1-score": 0.9697067997504679, "precision": 0.9531062222549236, "recall": 0.9868959037001295, "support": 39377}, "\u23ce": {"f1-score": 0.8119409660107335, "precision": 0.8860419716935091, "recall": 0.7492777548493603, "support": 4846}, "\u23ce\"": {"f1-score": 0.8813559322033897, "precision": 0.8253968253968254, "recall": 0.9454545454545454, "support": 55}, "\u23ce\u21e5\u207a": {"f1-score": 0.856140350877193, "precision": 0.9694080254270957, "recall": 0.7665724159597863, "support": 3183}, "\u23ce\u21e5\u207b": {"f1-score": 0.8755211435378202, "precision": 0.930379746835443, "recall": 0.8267716535433071, "support": 2667}, "\u23ce\u21e5\u207b\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 83}, "\u23ce\u23ce": {"f1-score": 0.7181254307374223, "precision": 0.877104377104377, "recall": 0.6079346557759626, "support": 857}, "\u23ce\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 15}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 10}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 10}, "\u2423": {"f1-score": 0.959950043995345, "precision": 0.944112556529507, "recall": 0.9763279445727483, "support": 17320}, "\u2423\"": {"f1-score": 0.9434151226840259, "precision": 0.9040307101727447, "recall": 0.9863874345549738, "support": 955}, "\u2423\u0027": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 22}},
  "cl_report_full": {"\"": {"f1-score": 0.9167064439140811, "precision": 0.9512134720158494, "recall": 0.8846153846153846, "support": 4342}, "\"\u23ce\u21e5\u207b": {"f1-score": 0.679245283018868, "precision": 0.9183673469387755, "recall": 0.5389221556886228, "support": 167}, "\"\u2423": {"f1-score": 0.7735191637630662, "precision": 0.9173553719008265, "recall": 0.6686746987951807, "support": 166}, "\u0027": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 29}, "\u0027\u2423": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 10}, "macro avg": {"f1-score": 0.5033424052381963, "precision": 0.5598064792372154, "recall": 0.46807205590463113, "support": 75888}, "micro avg": {"f1-score": 0.9305907440955672, "precision": 0.9443848961371993, "recall": 0.9171937592241197, "support": 75888}, "weighted avg": {"f1-score": 0.9255331613785917, "precision": 0.9413877129703382, "recall": 0.9171937592241197, "support": 75888}, "\u2205": {"f1-score": 0.9677387222492, "precision": 0.9531062222549236, "recall": 0.9828275164390491, "support": 39540}, "\u23ce": {"f1-score": 0.7543367611924795, "precision": 0.8860419716935091, "recall": 0.6567191173810816, "support": 5529}, "\u23ce\"": {"f1-score": 0.8813559322033897, "precision": 0.8253968253968254, "recall": 0.9454545454545454, "support": 55}, "\u23ce\u21e5\u207a": {"f1-score": 0.844582900657667, "precision": 0.9694080254270957, "recall": 0.7482367371971788, "support": 3261}, "\u23ce\u21e5\u207b": {"f1-score": 0.8403201219512195, "precision": 0.930379746835443, "recall": 0.7661570535093816, "support": 2878}, "\u23ce\u21e5\u207b\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 86}, "\u23ce\u23ce": {"f1-score": 0.5795328142380423, "precision": 0.877104377104377, "recall": 0.43272425249169433, "support": 1204}, "\u23ce\u23ce\u21e5\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 17}, "\u23ce\u2423\u207a\u2423\u207a": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 10}, "\u23ce\u2423\u207b\u2423\u207b": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 10}, "\u2423": {"f1-score": 0.9570163275701067, "precision": 0.944112556529507, "recall": 0.9702777140234106, "support": 17428}, "\u2423\"": {"f1-score": 0.8658088235294117, "precision": 0.9040307101727447, "recall": 0.8306878306878307, "support": 1134}, "\u2423\u0027": {"f1-score": 0.0, "precision": 0.0, "recall": 0.0, "support": 22}},
  "ppcr": 0.971207569049125
}
```
</details>