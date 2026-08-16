"""
Comprehensive knowledge base for 38 disease/healthy classes across 14 crops
(apple, blueberry, cherry, corn, grape, orange, peach, pepper, potato,
raspberry, soybean, squash, strawberry, tomato).
Used as RAG context for the AI chatbot to give accurate farming advice.
"""

PLANT_DISEASE_KNOWLEDGE = {
    # ------------------------------------------------------------------ #
    # Pepper
    # ------------------------------------------------------------------ #
    "Pepper__bell___Bacterial_spot": {
        "disease_name": "Pepper Bacterial Spot",
        "scientific_name": "Xanthomonas campestris pv. vesicatoria",
        "description": "Bacterial spot is a common and destructive disease of bell peppers caused by Xanthomonas bacteria. It affects leaves, stems, and fruit, reducing marketable yield.",
        "symptoms": [
            "Small, water-soaked circular spots on leaves that turn dark brown",
            "Spots may have a yellow halo and look greasy",
            "Leaves turn yellow and drop prematurely (defoliation)",
            "Raised, scab-like brown lesions on fruit",
            "Stem lesions can girdle young plants",
        ],
        "causes": [
            "Caused by Xanthomonas campestris pv. vesicatoria bacteria",
            "Spreads via wind-driven rain, overhead irrigation, and splashing water",
            "Enters through wounds, stomata, or hydathodes",
            "Survives on infected seed, plant debris, and volunteer plants",
            "Favoured by warm (24-30°C), humid, rainy weather",
        ],
        "treatment": [
            "Apply copper-based bactericides (bacteria are not controlled by fungicides)",
            "Combine copper with Mancozeb to slow resistance development",
            "Remove and destroy heavily infected plants",
            "Avoid working in fields when foliage is wet (spreads bacteria on hands/tools)",
        ],
        "prevention": [
            "Use certified disease-free seed and transplants",
            "Practice 2-3 year crop rotation away from peppers and tomatoes",
            "Avoid overhead irrigation — use drip irrigation instead",
            "Disinfect stakes, tools and equipment between fields",
            "Plant resistant/tolerant varieties where available",
            "Space plants for good airflow to reduce leaf wetness duration",
        ],
        "recommended_pesticides": [
            {
                "name": "Copper Hydroxide",
                "type": "Bactericide",
                "usage": "Spray every 7-10 days, especially before rain events",
            },
            {
                "name": "Copper + Mancozeb",
                "type": "Bactericide + Fungicide",
                "usage": "Mix as per label, apply preventively every 7 days",
            },
            {
                "name": "Streptomycin sulfate",
                "type": "Bactericide (where permitted)",
                "usage": "Use only where locally approved; follow label rate strictly",
            },
        ],
        "severity": "Moderate to High - can cause significant defoliation and fruit loss in wet seasons",
        "season": "Warm, humid, rainy periods; common in summer plantings",
    },
    "Pepper__bell___healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your bell pepper plant appears healthy! Here are some tips to keep it that way and maximize your yield.",
        "symptoms": [
            "Leaves are uniformly green, glossy, and firm",
            "No spots, lesions, or wilting",
            "Sturdy stems and good branching",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your plant looks healthy!",
            "Continue regular monitoring for early signs of disease or pests",
        ],
        "prevention": [
            "Water at the base, avoid wetting foliage",
            "Maintain balanced fertilization (NPK per soil test)",
            "Stake or cage plants to keep fruit off the ground",
            "Rotate crops and remove plant debris after harvest",
            "Scout weekly for aphids, thrips, and bacterial spot symptoms",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Apply balanced fertilizer at transplanting, side-dress mid-season",
            "Water deeply 1-2 inches per week, more in fruiting stage",
            "Mulch to conserve moisture and suppress weeds",
            "Harvest peppers regularly to encourage continued fruiting",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
    # ------------------------------------------------------------------ #
    # Potato
    # ------------------------------------------------------------------ #
    "Potato___Early_blight": {
        "disease_name": "Early Blight",
        "scientific_name": "Alternaria solani",
        "description": "Early blight is a common fungal disease of potatoes caused by Alternaria solani. It primarily affects leaves but can also infect stems and tubers.",
        "symptoms": [
            "Dark brown to black circular spots on lower (older) leaves first",
            "Spots have characteristic concentric rings (target-like or bull's-eye pattern)",
            "Yellow halo around the spots",
            "Leaves eventually turn yellow and drop off",
            "Stem lesions appear as dark, elongated spots",
            "Tuber lesions are dark, sunken, and circular with raised borders",
        ],
        "causes": [
            "Caused by the fungus Alternaria solani",
            "Spreads through wind, rain splash, and contaminated equipment",
            "Thrives in warm (24-29°C / 75-84°F) and humid conditions",
            "Overwinters in infected plant debris and soil",
            "Stressed plants (nutrient deficiency, drought) are more susceptible",
        ],
        "treatment": [
            "Apply fungicides like Chlorothalonil, Mancozeb, or Azoxystrobin",
            "Start fungicide applications when symptoms first appear",
            "Spray every 7-10 days during favorable disease conditions",
            "Remove and destroy infected leaves and plant debris",
            "Apply copper-based fungicides as an organic alternative",
            "Use neem oil spray (organic option) as preventive measure",
        ],
        "prevention": [
            "Practice crop rotation (3-4 year rotation away from potatoes and tomatoes)",
            "Use certified disease-free seed potatoes",
            "Plant resistant varieties when available",
            "Maintain adequate plant spacing for good air circulation",
            "Water at the base of plants, avoid overhead irrigation",
            "Mulch around plants to prevent soil splash onto leaves",
            "Keep plants well-fertilized, especially with nitrogen and potassium",
            "Remove and destroy all plant debris after harvest",
        ],
        "recommended_pesticides": [
            {
                "name": "Mancozeb",
                "type": "Fungicide",
                "usage": "Mix 2-3 grams per liter of water, spray every 7-10 days",
            },
            {
                "name": "Chlorothalonil (Daconil)",
                "type": "Fungicide",
                "usage": "Mix as per label, apply preventively every 7-14 days",
            },
            {
                "name": "Azoxystrobin (Amistar)",
                "type": "Systemic Fungicide",
                "usage": "Apply at first sign of disease, repeat every 14 days",
            },
            {
                "name": "Copper Oxychloride",
                "type": "Organic Fungicide",
                "usage": "Mix 3 grams per liter, spray every 7-10 days",
            },
            {
                "name": "Neem Oil",
                "type": "Organic",
                "usage": "Mix 5ml per liter of water, spray weekly as prevention",
            },
        ],
        "severity": "Moderate to High - Can cause 20-50% yield loss if untreated",
        "season": "Most common in warm, humid weather, typically mid to late growing season",
    },
    "Potato___Late_blight": {
        "disease_name": "Late Blight",
        "scientific_name": "Phytophthora infestans",
        "description": "Late blight is a devastating disease caused by the water mold Phytophthora infestans. It was responsible for the Irish Potato Famine (1845-1849). It can destroy entire fields within days under favorable conditions.",
        "symptoms": [
            "Water-soaked, pale green to dark spots on leaf tips and edges",
            "White fuzzy mold growth on the underside of leaves (in humid conditions)",
            "Spots rapidly enlarge and turn dark brown to black",
            "Entire leaves and stems can be destroyed very quickly",
            "A distinctive foul smell from rotting tissue",
            "Tubers develop reddish-brown dry rot that extends into the flesh",
            "Under wet conditions, entire plants can collapse within 1-2 weeks",
        ],
        "causes": [
            "Caused by the oomycete (water mold) Phytophthora infestans",
            "Spreads extremely rapidly through wind-blown spores",
            "Thrives in cool (10-25°C / 50-77°F) and wet/humid conditions",
            "Can spread through infected seed potatoes",
            "Rain and fog greatly increase disease spread",
            "Can survive in volunteer potato plants and cull piles",
        ],
        "treatment": [
            "IMMEDIATE ACTION REQUIRED - Late blight spreads very fast!",
            "Apply systemic fungicides like Metalaxyl (Ridomil) or Cymoxanil",
            "Use contact fungicides like Mancozeb in combination with systemics",
            "Spray every 5-7 days during active disease",
            "Remove and destroy ALL infected plants immediately",
            "Do NOT compost infected material - burn or bury deeply",
            "Harvest tubers as soon as possible from infected fields",
            "Apply phosphorous acid-based products (e.g., Agri-Fos)",
        ],
        "prevention": [
            "Use certified disease-free seed potatoes ALWAYS",
            "Plant resistant varieties (very important for late blight)",
            "Apply preventive fungicides before disease appears during high-risk periods",
            "Monitor weather forecasts - cool, wet weather increases risk",
            "Maintain good field drainage to reduce humidity",
            "Destroy all volunteer potato plants and cull piles",
            "Practice crop rotation (minimum 3 years)",
            "Hill potatoes well to protect tubers from spore wash",
            "Avoid overhead irrigation",
            "Scout fields regularly, especially during cool, wet weather",
        ],
        "recommended_pesticides": [
            {
                "name": "Metalaxyl + Mancozeb (Ridomil Gold)",
                "type": "Systemic + Contact Fungicide",
                "usage": "Mix 2.5g per liter, apply every 7 days during high risk",
            },
            {
                "name": "Cymoxanil + Mancozeb (Curzate)",
                "type": "Systemic + Contact Fungicide",
                "usage": "Mix as per label, apply every 5-7 days",
            },
            {
                "name": "Dimethomorph (Acrobat)",
                "type": "Systemic Fungicide",
                "usage": "Apply preventively or at first symptoms",
            },
            {
                "name": "Mandipropamid (Revus)",
                "type": "Systemic Fungicide",
                "usage": "Apply every 7-10 days as prevention",
            },
            {
                "name": "Copper Hydroxide",
                "type": "Organic Fungicide",
                "usage": "Mix 2-3g per liter, spray every 5-7 days",
            },
            {
                "name": "Phosphorous Acid (Agri-Fos)",
                "type": "Systemic",
                "usage": "Apply as foliar spray or soil drench",
            },
        ],
        "severity": "VERY HIGH - Can cause 100% crop loss if not treated immediately!",
        "season": "Most dangerous in cool, wet conditions - spring and fall in temperate regions",
    },
    "Potato___healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your potato plant appears healthy! Here are some tips to keep it that way and maximize your yield.",
        "symptoms": [
            "Leaves are uniformly green and firm",
            "No spots, discoloration, or wilting",
            "Strong, sturdy stems",
            "Good overall plant vigor",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your plant looks healthy!",
            "Continue regular monitoring for any signs of disease",
            "Maintain your current farming practices",
        ],
        "prevention": [
            "Continue regular crop scouting (check plants weekly)",
            "Maintain balanced fertilization (NPK as per soil test)",
            "Water consistently but avoid overwatering",
            "Practice crop rotation to prevent disease buildup",
            "Use certified disease-free seed potatoes",
            "Keep fields clean of debris and weeds",
            "Monitor weather conditions for disease-favorable periods",
            "Apply preventive fungicides during high-risk weather",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Apply balanced fertilizer (NPK 10-10-20 or similar) at planting",
            "Side-dress with nitrogen 3-4 weeks after emergence",
            "Hill plants when they are 6-8 inches tall to protect tubers",
            "Water deeply but infrequently (1-2 inches per week)",
            "Mulch between rows to conserve moisture and suppress weeds",
            "Monitor for insect pests like Colorado potato beetle and aphids",
            "Harvest when plant tops begin to die back naturally",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
    # ------------------------------------------------------------------ #
    # Tomato
    # ------------------------------------------------------------------ #
    "Tomato_Bacterial_spot": {
        "disease_name": "Tomato Bacterial Spot",
        "scientific_name": "Xanthomonas spp.",
        "description": "Bacterial spot causes small dark lesions on tomato leaves, stems and fruit, reducing both yield and fruit quality.",
        "symptoms": [
            "Small, water-soaked spots on leaves that turn dark brown to black",
            "Spots may merge, causing large necrotic areas and leaf drop",
            "Raised, scabby brown spots with a greasy halo on fruit",
            "Defoliation exposes fruit to sunscald",
        ],
        "causes": [
            "Caused by Xanthomonas bacteria species",
            "Spread by splashing rain, overhead irrigation, and contaminated tools/hands",
            "Enters through wounds and natural openings",
            "Favoured by warm, wet, humid weather",
            "Survives on infected seed and plant debris",
        ],
        "treatment": [
            "Apply copper-based bactericides, ideally mixed with Mancozeb",
            "Remove and destroy severely infected plants and debris",
            "Avoid handling wet plants to prevent spreading bacteria",
        ],
        "prevention": [
            "Use certified disease-free seed and transplants",
            "Rotate crops for at least 2 years away from tomatoes/peppers",
            "Use drip irrigation instead of overhead sprinklers",
            "Stake/cage plants for better airflow",
            "Disinfect tools and stakes between uses",
        ],
        "recommended_pesticides": [
            {
                "name": "Copper Hydroxide",
                "type": "Bactericide",
                "usage": "Spray every 7-10 days, more often in wet weather",
            },
            {
                "name": "Copper + Mancozeb",
                "type": "Bactericide + Fungicide",
                "usage": "Apply preventively every 7 days",
            },
        ],
        "severity": "Moderate to High - significant yield and fruit-quality loss in wet seasons",
        "season": "Warm, humid, rainy weather",
    },
    "Tomato_Early_blight": {
        "disease_name": "Tomato Early Blight",
        "scientific_name": "Alternaria solani / A. tomatophila",
        "description": "Early blight is one of the most common fungal diseases of tomato, causing leaf spots and defoliation that reduce yield and fruit quality.",
        "symptoms": [
            "Dark brown spots with concentric rings (target/bull's-eye pattern) on older leaves first",
            "Yellowing of tissue surrounding spots",
            "Progressive defoliation from the bottom of the plant upward",
            "Dark, sunken lesions can also appear on stems and fruit near the stem end",
        ],
        "causes": [
            "Caused by Alternaria fungi",
            "Spread by wind, rain splash, and contaminated tools",
            "Favoured by warm temperatures and high humidity/leaf wetness",
            "Overwinters in plant debris and soil",
            "Stressed or nutrient-deficient plants are more susceptible",
        ],
        "treatment": [
            "Apply fungicides such as Chlorothalonil, Mancozeb, or Azoxystrobin at first symptoms",
            "Repeat every 7-10 days during favorable conditions",
            "Remove and destroy infected lower leaves",
            "Use copper-based fungicide or neem oil as organic options",
        ],
        "prevention": [
            "Rotate crops (avoid tomato/potato for 2-3 years)",
            "Stake and prune plants for airflow, mulch to reduce soil splash",
            "Water at the base, avoid overhead irrigation",
            "Choose resistant varieties where available",
            "Remove plant debris at end of season",
        ],
        "recommended_pesticides": [
            {
                "name": "Chlorothalonil",
                "type": "Fungicide",
                "usage": "Apply preventively every 7-14 days",
            },
            {
                "name": "Mancozeb",
                "type": "Fungicide",
                "usage": "Mix 2-3g per liter, spray every 7-10 days",
            },
            {
                "name": "Azoxystrobin",
                "type": "Systemic Fungicide",
                "usage": "Apply at first sign of disease, repeat every 14 days",
            },
            {"name": "Copper Fungicide", "type": "Organic", "usage": "Spray every 7-10 days"},
        ],
        "severity": "Moderate to High - can cause substantial defoliation and yield loss",
        "season": "Warm, humid weather; mid-to-late season",
    },
    "Tomato_Late_blight": {
        "disease_name": "Tomato Late Blight",
        "scientific_name": "Phytophthora infestans",
        "description": "The same pathogen that causes potato late blight; it can devastate tomato crops within days under cool, wet conditions.",
        "symptoms": [
            "Water-soaked, irregular pale-green to brown lesions on leaves, often starting at leaf edges",
            "White fuzzy fungal growth on leaf undersides in humid conditions",
            "Rapid blackening and collapse of foliage and stems",
            "Firm, brown, greasy-looking lesions on fruit that can rot quickly",
        ],
        "causes": [
            "Caused by the oomycete Phytophthora infestans",
            "Spreads rapidly via wind-blown spores over long distances",
            "Thrives in cool, wet, humid weather",
            "Can spread from nearby infected potato crops",
        ],
        "treatment": [
            "IMMEDIATE ACTION REQUIRED - spreads extremely fast",
            "Apply systemic fungicides (Metalaxyl, Cymoxanil) combined with a contact fungicide like Mancozeb",
            "Spray every 5-7 days during active outbreaks",
            "Remove and destroy infected plants immediately - do not compost",
        ],
        "prevention": [
            "Plant resistant/tolerant varieties",
            "Avoid planting near potato fields",
            "Improve airflow via staking/pruning, avoid overhead irrigation",
            "Monitor weather - cool, wet forecasts mean high risk",
            "Apply preventive fungicide sprays ahead of high-risk periods",
        ],
        "recommended_pesticides": [
            {
                "name": "Metalaxyl + Mancozeb",
                "type": "Systemic + Contact Fungicide",
                "usage": "Apply every 7 days during high risk periods",
            },
            {
                "name": "Cymoxanil + Mancozeb (Curzate)",
                "type": "Systemic + Contact Fungicide",
                "usage": "Apply every 5-7 days",
            },
            {
                "name": "Chlorothalonil",
                "type": "Contact Fungicide",
                "usage": "Apply preventively every 7 days",
            },
        ],
        "severity": "VERY HIGH - can destroy entire crop within days if untreated",
        "season": "Cool, wet weather - typically early spring or fall",
    },
    "Tomato_Leaf_Mold": {
        "disease_name": "Tomato Leaf Mold",
        "scientific_name": "Passalora fulva (syn. Fulvia fulva / Cladosporium fulvum)",
        "description": "Leaf mold is a fungal disease especially problematic in greenhouse and high-humidity tomato production, affecting foliage and reducing photosynthesis.",
        "symptoms": [
            "Pale green to yellow spots on the upper leaf surface",
            "Olive-green to grayish-purple velvety mold on the corresponding leaf underside",
            "Leaves curl, wither, and drop as the disease progresses",
            "Rarely affects fruit directly",
        ],
        "causes": [
            "Caused by the fungus Passalora fulva",
            "Favoured by high humidity (>85%) and moderate temperatures",
            "Very common in greenhouses/polytunnels with poor ventilation",
            "Spreads via airborne spores and water splash",
        ],
        "treatment": [
            "Improve ventilation and reduce humidity immediately",
            "Apply fungicides such as Chlorothalonil, Mancozeb, or Copper-based products",
            "Remove and destroy heavily infected leaves",
        ],
        "prevention": [
            "Ventilate greenhouses well; use fans to reduce leaf wetness",
            "Space plants properly and prune for airflow",
            "Water at the base early in the day so foliage dries quickly",
            "Choose resistant varieties where available",
            "Sanitize greenhouse structures between seasons",
        ],
        "recommended_pesticides": [
            {
                "name": "Chlorothalonil",
                "type": "Fungicide",
                "usage": "Apply every 7-10 days during high humidity periods",
            },
            {"name": "Copper Fungicide", "type": "Organic", "usage": "Spray every 7-10 days"},
            {
                "name": "Mancozeb",
                "type": "Fungicide",
                "usage": "Apply as per label every 7-10 days",
            },
        ],
        "severity": "Moderate - mainly a greenhouse problem, reduces yield through leaf loss",
        "season": "High humidity conditions, common in greenhouse production year-round",
    },
    "Tomato_Septoria_leaf_spot": {
        "disease_name": "Tomato Septoria Leaf Spot",
        "scientific_name": "Septoria lycopersici",
        "description": "Septoria leaf spot is a widespread fungal disease that causes progressive defoliation starting from the lower leaves, weakening the plant and exposing fruit to sunscald.",
        "symptoms": [
            "Small, circular spots with dark brown margins and gray/tan centers on lower leaves first",
            "Tiny black fruiting bodies (pycnidia) visible in the center of older spots",
            "Severe infections cause yellowing and dropping of leaves from the bottom up",
            "Rarely affects fruit",
        ],
        "causes": [
            "Caused by the fungus Septoria lycopersici",
            "Spreads via rain splash, overhead irrigation, and contaminated tools",
            "Favoured by warm, wet weather and prolonged leaf wetness",
            "Overwinters in plant debris and on volunteer tomato plants",
        ],
        "treatment": [
            "Apply fungicides (Chlorothalonil, Mancozeb, Copper) at first sign of spots",
            "Repeat every 7-10 days, especially in wet weather",
            "Remove and destroy infected lower leaves promptly",
        ],
        "prevention": [
            "Rotate crops away from tomato/potato for 2-3 years",
            "Mulch to prevent soil splash onto lower leaves",
            "Stake/prune for airflow, water at the base",
            "Remove volunteer tomato plants and clean up debris after harvest",
        ],
        "recommended_pesticides": [
            {
                "name": "Chlorothalonil",
                "type": "Fungicide",
                "usage": "Apply preventively every 7-10 days",
            },
            {
                "name": "Mancozeb",
                "type": "Fungicide",
                "usage": "Mix 2-3g per liter, spray every 7-10 days",
            },
            {"name": "Copper Fungicide", "type": "Organic", "usage": "Spray every 7-10 days"},
        ],
        "severity": "Moderate to High - progressive defoliation can significantly reduce yield",
        "season": "Warm, wet weather; common mid-to-late season",
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "disease_name": "Two-Spotted Spider Mite Damage",
        "scientific_name": "Tetranychus urticae",
        "description": "Not a disease but a pest infestation — tiny spider mites feed on leaf undersides, causing stippling and, in heavy infestations, webbing and plant decline.",
        "symptoms": [
            "Fine yellow/white stippling (tiny dots) on leaf upper surfaces",
            "Leaves appear bronzed, speckled, or dusty",
            "Fine webbing visible on leaf undersides and between stems in heavy infestations",
            "Leaves may yellow, dry out, and drop in severe cases",
        ],
        "causes": [
            "Caused by Tetranychus urticae, a tiny sap-sucking arachnid (not an insect)",
            "Thrives in hot, dry, dusty conditions",
            "Populations explode rapidly in drought-stressed plants",
            "Spreads by wind, on clothing/tools, and from nearby infested plants",
        ],
        "treatment": [
            "Spray plants (including leaf undersides) with water to dislodge mites",
            "Apply insecticidal soap or horticultural oil, targeting leaf undersides",
            "Use miticides (e.g., Abamectin, Bifenazate) for severe infestations",
            "Introduce natural predators like predatory mites (Phytoseiulus persimilis) or ladybugs",
        ],
        "prevention": [
            "Avoid drought stress - maintain consistent watering",
            "Reduce dust around plants (mites thrive in dusty conditions)",
            "Avoid excessive nitrogen fertilization which favors mite reproduction",
            "Monitor regularly, especially in hot, dry weather",
            "Encourage beneficial predatory insects/mites in the garden",
        ],
        "recommended_pesticides": [
            {
                "name": "Insecticidal Soap",
                "type": "Contact / Organic",
                "usage": "Spray thoroughly on leaf undersides every 5-7 days",
            },
            {
                "name": "Horticultural Oil (Neem/Mineral)",
                "type": "Contact / Organic",
                "usage": "Apply every 7 days, avoid spraying in direct sun/heat",
            },
            {
                "name": "Abamectin",
                "type": "Miticide",
                "usage": "Apply per label for severe infestations, rotate with other modes of action",
            },
        ],
        "severity": "Moderate to High in hot/dry conditions - can weaken plants and reduce yield",
        "season": "Hot, dry weather - most problematic in summer",
    },
    "Tomato__Target_Spot": {
        "disease_name": "Tomato Target Spot",
        "scientific_name": "Corynespora cassiicola",
        "description": "Target spot is a fungal disease causing leaf, stem and fruit lesions with a distinctive target-like pattern, capable of rapid defoliation in warm, humid climates.",
        "symptoms": [
            "Small water-soaked spots that enlarge into brown lesions with concentric rings",
            "Lesions can merge causing large necrotic patches and severe defoliation",
            "Sunken, dark lesions on fruit with concentric ring patterns",
            "Stem lesions can girdle young growth",
        ],
        "causes": [
            "Caused by the fungus Corynespora cassiicola",
            "Favoured by warm temperatures and high humidity/extended leaf wetness",
            "Spreads via wind-blown spores and water splash",
            "Survives in plant debris between seasons",
        ],
        "treatment": [
            "Apply fungicides such as Azoxystrobin, Chlorothalonil, or Mancozeb",
            "Begin applications at first sign of disease, repeat every 7-10 days",
            "Remove and destroy heavily infected leaves and fruit",
        ],
        "prevention": [
            "Rotate crops away from tomato for 1-2 years",
            "Improve airflow through staking/pruning and proper spacing",
            "Avoid overhead irrigation, water at the base",
            "Remove crop debris after harvest",
        ],
        "recommended_pesticides": [
            {
                "name": "Azoxystrobin",
                "type": "Systemic Fungicide",
                "usage": "Apply at first symptoms, repeat every 14 days",
            },
            {
                "name": "Chlorothalonil",
                "type": "Fungicide",
                "usage": "Apply preventively every 7-10 days",
            },
            {
                "name": "Mancozeb",
                "type": "Fungicide",
                "usage": "Mix 2-3g per liter, spray every 7-10 days",
            },
        ],
        "severity": "Moderate to High - can cause rapid defoliation in favorable conditions",
        "season": "Warm, humid weather; common in tropical/subtropical growing regions",
    },
    "Tomato__Tomato_YellowLeaf__Curl_Virus": {
        "disease_name": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "scientific_name": "Tomato yellow leaf curl virus (Begomovirus)",
        "description": "TYLCV is a devastating viral disease transmitted by whiteflies. Infection early in plant development can cause near-total yield loss.",
        "symptoms": [
            "Severe upward curling and crumpling of leaves",
            "Marked yellowing (chlorosis) of leaf margins and interveinal areas",
            "Stunted, bushy plant growth with shortened internodes",
            "Flower drop and drastically reduced fruit set",
        ],
        "causes": [
            "Caused by a Begomovirus transmitted exclusively by the whitefly Bemisia tabaci",
            "Not spread mechanically (not by touch/tools) - whitefly transmission only",
            "Whitefly populations build up rapidly in warm weather",
            "Weeds and other crops can act as a virus reservoir between seasons",
        ],
        "treatment": [
            "There is NO cure once a plant is infected - focus on whitefly control and removal",
            "Remove and destroy infected plants immediately to reduce virus reservoir",
            "Control whitefly vectors with insecticidal soap, neem oil, or systemic insecticides (Imidacloprid)",
            "Use yellow sticky traps to monitor and reduce whitefly populations",
        ],
        "prevention": [
            "Plant TYLCV-resistant/tolerant tomato varieties",
            "Use reflective mulches to repel whiteflies",
            "Install fine mesh screens/row covers on seedlings and young transplants",
            "Control weeds that host whiteflies around the field",
            "Avoid planting new tomatoes near existing infected plantings",
            "Manage whitefly populations proactively before symptoms appear",
        ],
        "recommended_pesticides": [
            {
                "name": "Imidacloprid",
                "type": "Systemic Insecticide (whitefly control)",
                "usage": "Apply as soil drench at transplanting per label",
            },
            {
                "name": "Insecticidal Soap",
                "type": "Contact / Organic",
                "usage": "Spray on leaf undersides to reduce whitefly nymphs",
            },
            {
                "name": "Neem Oil",
                "type": "Organic",
                "usage": "Apply every 7 days to disrupt whitefly life cycle",
            },
        ],
        "severity": "VERY HIGH - can cause up to 100% yield loss if plants are infected young",
        "season": "Warm weather when whitefly populations are high, typically summer",
    },
    "Tomato__Tomato_mosaic_virus": {
        "disease_name": "Tomato Mosaic Virus (ToMV)",
        "scientific_name": "Tomato mosaic virus",
        "description": "ToMV is a highly stable and easily spread virus causing mottling and distortion of leaves and fruit, reducing yield and quality.",
        "symptoms": [
            "Light and dark green mottled/mosaic pattern on leaves",
            "Leaf distortion - narrowing, curling, or fern-like leaves",
            "Stunted plant growth",
            "Internal browning or mottling of fruit; uneven ripening",
        ],
        "causes": [
            "Caused by Tomato mosaic virus, extremely stable and long-lived in plant debris and soil",
            "Spreads mechanically through handling, tools, and contaminated hands/clothing",
            "Can be seed-borne",
            "Does NOT require an insect vector - human handling is the main spread route",
        ],
        "treatment": [
            "There is NO cure - remove and destroy infected plants immediately",
            "Wash hands and disinfect tools thoroughly after handling infected plants",
            "Avoid handling plants while smoking/using tobacco products (virus can be present in tobacco)",
        ],
        "prevention": [
            "Use certified virus-free seed, or treat seed as recommended",
            "Plant resistant varieties (Tm resistance genes) where available",
            "Disinfect tools, stakes and hands between plants (10% bleach or trisodium phosphate solution)",
            "Avoid working with tomato plants after handling tobacco products",
            "Remove and destroy all infected plant debris - do not compost",
            "Rotate crops and control weeds that may harbor the virus",
        ],
        "recommended_pesticides": [],
        "severity": "High - reduces yield and fruit quality, no chemical treatment available",
        "season": "Can occur any time; spread accelerated by frequent handling (pruning, tying, harvesting)",
    },
    "Tomato_healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your tomato plant appears healthy! Here are some tips to keep it that way and maximize your yield.",
        "symptoms": [
            "Leaves are uniformly green and firm",
            "No spots, mottling, curling, or wilting",
            "Strong stems with good branching and flowering",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your plant looks healthy!",
            "Continue regular monitoring for early signs of disease or pests",
        ],
        "prevention": [
            "Water at the base early in the day, avoid wetting foliage",
            "Stake/cage plants and prune for good airflow",
            "Maintain balanced fertilization (NPK per soil test)",
            "Rotate crops and remove plant debris after harvest",
            "Scout weekly for whiteflies, spider mites, and early leaf-spot symptoms",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Apply balanced fertilizer at transplanting, side-dress during fruiting",
            "Water deeply and consistently - 1-2 inches per week",
            "Mulch to conserve moisture and reduce soil splash onto leaves",
            "Remove suckers and lower leaves touching the soil",
            "Harvest regularly to encourage continued fruit production",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
    # ------------------------------------------------------------------ #
    # Apple
    # ------------------------------------------------------------------ #
    "Apple___Apple_scab": {
        "disease_name": "Apple Scab",
        "scientific_name": "Venturia inaequalis",
        "description": "Apple scab is one of the most common and serious fungal diseases of apple, causing olive-green to black lesions on leaves and fruit that reduce marketability and, in severe cases, defoliate the tree.",
        "symptoms": [
            "Olive-green to brown/black velvety spots on leaves, often on the underside first",
            "Similar dark, scabby lesions on fruit that can crack as fruit grows",
            "Infected leaves may pucker, curl, and drop early",
            "Severe infections cause significant premature defoliation",
        ],
        "causes": [
            "Caused by the fungus Venturia inaequalis",
            "Overwinters in fallen leaf litter and releases spores in spring",
            "Spreads via wind and rain-splashed spores during wet spring weather",
            "Favoured by cool, wet spring conditions with extended leaf wetness",
        ],
        "treatment": [
            "Apply fungicides (captan, myclobutanil, or sulfur-based products) starting at green tip stage",
            "Continue protectant sprays through the primary infection period (spring rains)",
            "Remove and destroy fallen leaves in autumn to reduce overwintering spores",
            "Prune for better air circulation to speed leaf drying",
        ],
        "prevention": [
            "Plant scab-resistant apple varieties where possible",
            "Rake up and destroy fallen leaves every autumn",
            "Avoid overhead irrigation late in the day",
            "Prune to open the canopy and improve airflow/sun penetration",
            "Apply a dormant-season fungicide spray in high-pressure orchards",
        ],
        "recommended_pesticides": [
            {
                "name": "Captan",
                "type": "Fungicide",
                "usage": "Apply as a protectant spray every 7-10 days during wet spring weather",
            },
            {
                "name": "Myclobutanil",
                "type": "Systemic Fungicide",
                "usage": "Apply at green tip and repeat per label through petal fall",
            },
            {
                "name": "Sulfur",
                "type": "Fungicide (organic option)",
                "usage": "Apply preventively; avoid during high heat to prevent leaf burn",
            },
        ],
        "severity": "Moderate to High - can cause major fruit loss and defoliation in wet years",
        "season": "Cool, wet spring weather during leaf and fruit development",
    },
    "Apple___Black_rot": {
        "disease_name": "Apple Black Rot",
        "scientific_name": "Botryosphaeria obtusa",
        "description": "Black rot affects apple leaves, fruit, and bark, causing leaf spots, fruit rot, and cankers on branches. It's especially damaging on trees stressed by winter injury, drought, or poor nutrition.",
        "symptoms": [
            'Purple-bordered brown leaf spots ("frog-eye leaf spot")',
            "Fruit rot starting at the calyx end, turning black and mummified",
            "Concentric rings visible on rotted fruit",
            "Sunken, reddish-brown cankers on branches and trunk",
        ],
        "causes": [
            "Caused by the fungus Botryosphaeria obtusa",
            "Enters through wounds, dead wood, and winter-injured tissue",
            "Overwinters in cankers, mummified fruit, and dead bark",
            "Favoured by warm, humid weather and tree stress",
        ],
        "treatment": [
            "Prune out and destroy cankered wood and mummified fruit",
            "Apply fungicides (captan or thiophanate-methyl) during the growing season",
            "Remove dead or weakened branches promptly",
            "Improve overall tree vigor with proper fertilization and watering",
        ],
        "prevention": [
            "Remove mummified fruit and dead wood every dormant season",
            "Avoid unnecessary wounding of bark and branches",
            "Maintain tree vigor - stressed trees are far more susceptible",
            "Ensure good air circulation through proper pruning",
        ],
        "recommended_pesticides": [
            {
                "name": "Captan",
                "type": "Fungicide",
                "usage": "Apply during the cover spray period per regional extension guidelines",
            },
            {
                "name": "Thiophanate-methyl",
                "type": "Systemic Fungicide",
                "usage": "Apply per label, especially after pruning wounds",
            },
        ],
        "severity": "Moderate - primarily affects stressed or wounded trees, can cause fruit loss",
        "season": "Warm, humid summer weather; canker infections can occur year-round",
    },
    "Apple___Cedar_apple_rust": {
        "disease_name": "Cedar Apple Rust",
        "scientific_name": "Gymnosporangium juniperi-virginianae",
        "description": "Cedar apple rust is a fungal disease that requires both apple/crabapple and cedar/juniper trees to complete its life cycle, causing bright orange leaf spots on apple and galls on cedar.",
        "symptoms": [
            "Small yellow spots on upper leaf surface that enlarge and turn bright orange",
            "Black dots (spermogonia) appear within the orange leaf spots",
            "Orange, tube-like structures on the underside of leaves later in season",
            "Premature leaf drop in heavy infections",
            "Fruit may show yellow-orange spots and become distorted",
        ],
        "causes": [
            "Caused by the fungus Gymnosporangium juniperi-virginianae",
            "Requires a nearby cedar or juniper host to complete its life cycle",
            "Spores travel from cedar galls to apple trees in spring rains",
            "Favoured by wet spring weather and proximity to eastern redcedar",
        ],
        "treatment": [
            "Apply fungicides (myclobutanil or propiconazole) starting at pink bud stage",
            "Continue sprays through several weeks after petal fall",
            "Remove nearby cedar/juniper trees if practical (within a few hundred meters)",
            "Prune out visible galls on any nearby cedar trees before spring",
        ],
        "prevention": [
            "Plant rust-resistant apple varieties",
            "Avoid planting apples near cedar or juniper trees when possible",
            "Remove galls from nearby junipers in late winter before they release spores",
            "Apply preventive fungicide in high-pressure areas",
        ],
        "recommended_pesticides": [
            {
                "name": "Myclobutanil",
                "type": "Systemic Fungicide",
                "usage": "Apply at pink bud stage and repeat per label through early summer",
            },
            {
                "name": "Propiconazole",
                "type": "Systemic Fungicide",
                "usage": "Apply preventively before spring rains begin",
            },
        ],
        "severity": "Low to Moderate - mainly cosmetic on leaves, but can reduce fruit quality and yield",
        "season": "Spring, during wet weather when cedar galls release spores",
    },
    "Apple___healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your apple tree appears healthy! Here are some tips to keep it productive and disease-free.",
        "symptoms": [
            "Leaves are uniformly green with no spots or discoloration",
            "No fruit lesions, cracking, or premature drop",
            "Healthy bark with no cankers or oozing",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your tree looks healthy!",
            "Continue regular monitoring, especially after wet spring weather",
        ],
        "prevention": [
            "Rake and destroy fallen leaves each autumn to reduce fungal spores",
            "Prune annually for good light penetration and airflow",
            "Avoid wetting foliage with irrigation - water at the base",
            "Apply a balanced dormant-season spray program in disease-prone areas",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Fertilize based on a soil test, avoiding excess nitrogen",
            "Thin fruit to improve size and reduce limb stress",
            "Water deeply during dry spells, especially in the first few years",
            "Monitor for pests like codling moth and aphids regularly",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
    # ------------------------------------------------------------------ #
    # Blueberry
    # ------------------------------------------------------------------ #
    "Blueberry___healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your blueberry bush appears healthy! Here are some tips to keep it productive.",
        "symptoms": [
            "Leaves are uniformly green with good color",
            "No leaf spots, scorch, or premature reddening outside of autumn",
            "Firm, plump berries and vigorous new cane growth",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your plant looks healthy!",
            "Continue regular monitoring for pests and early disease signs",
        ],
        "prevention": [
            "Maintain acidic soil (pH 4.5-5.5) - blueberries are very pH sensitive",
            "Mulch with pine bark or sawdust to retain moisture and suppress weeds",
            "Prune out old, unproductive canes each dormant season",
            "Ensure good drainage - blueberries dislike waterlogged roots",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Water consistently - shallow roots are sensitive to drought stress",
            "Fertilize with an acid-forming, ammonium-based fertilizer in spring",
            "Net bushes to protect ripening berries from birds",
            "Test soil pH annually and amend with sulfur if needed",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
    # ------------------------------------------------------------------ #
    # Cherry
    # ------------------------------------------------------------------ #
    "Cherry___Powdery_mildew": {
        "disease_name": "Cherry Powdery Mildew",
        "scientific_name": "Podosphaera clandestina",
        "description": "Powdery mildew is a common fungal disease of cherry trees, coating leaves, shoots, and sometimes fruit with a white, powdery growth that weakens the tree and reduces fruit quality.",
        "symptoms": [
            "White, powdery fungal growth on leaves, shoots, and buds",
            "Leaves may curl, pucker, or show pale green/yellow blotches",
            "Infected shoot tips become stunted and distorted",
            "Fruit can develop white patches and russeting on the skin",
        ],
        "causes": [
            "Caused by the fungus Podosphaera clandestina",
            "Overwinters in infected buds",
            "Spreads via windborne spores, unlike most fungi does not need free water to infect",
            "Favoured by warm days, cool nights, and high humidity (but not rain)",
        ],
        "treatment": [
            "Apply fungicides (sulfur, myclobutanil, or potassium bicarbonate) at first sign of disease",
            "Prune out and destroy infected shoots",
            "Improve air circulation through canopy thinning",
            "Repeat sprays per label during the susceptible growing period",
        ],
        "prevention": [
            "Plant resistant cherry varieties where available",
            "Avoid excess nitrogen fertilization, which promotes susceptible new growth",
            "Prune to open the canopy and improve sunlight penetration",
            "Remove water sprouts and suckers that are highly susceptible",
        ],
        "recommended_pesticides": [
            {
                "name": "Sulfur",
                "type": "Fungicide (organic option)",
                "usage": "Apply at first sign of white growth; avoid in high heat",
            },
            {
                "name": "Myclobutanil",
                "type": "Systemic Fungicide",
                "usage": "Apply per label, rotate with other fungicide classes to prevent resistance",
            },
            {
                "name": "Potassium bicarbonate",
                "type": "Fungicide (organic option)",
                "usage": "Contact fungicide, apply every 7-14 days",
            },
        ],
        "severity": "Moderate - reduces fruit quality and tree vigor, rarely fatal",
        "season": "Warm days with cool nights and high humidity, typically late spring to summer",
    },
    "Cherry___healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your cherry tree appears healthy! Here are some tips to keep it that way.",
        "symptoms": [
            "Leaves are uniformly green with no powdery coating or spots",
            "No shoot dieback or distorted growth",
            "Firm, well-colored fruit at harvest",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your tree looks healthy!",
            "Continue regular monitoring, especially during warm, humid weather",
        ],
        "prevention": [
            "Prune annually to maintain an open canopy",
            "Avoid excess nitrogen fertilizer",
            "Water at the base and avoid wetting foliage late in the day",
            "Remove fallen fruit and leaf debris to reduce disease carryover",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Fertilize based on soil test results, split applications through the season",
            "Thin fruit if heavily set to improve size and reduce limb stress",
            "Net trees to protect ripening cherries from birds",
            "Monitor for brown rot and cherry fruit fly during fruit development",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
    # ------------------------------------------------------------------ #
    # Corn (Maize)
    # ------------------------------------------------------------------ #
    "Corn___Cercospora_Gray_leaf_spot": {
        "disease_name": "Corn Gray Leaf Spot",
        "scientific_name": "Cercospora zeae-maydis",
        "description": "Gray leaf spot is one of the most yield-limiting foliar diseases of corn, producing rectangular lesions on leaves that reduce photosynthetic area and can lead to premature plant death.",
        "symptoms": [
            "Small, tan, water-soaked spots that expand into rectangular lesions",
            "Lesions run parallel to leaf veins, tan to gray in color",
            "Lesions can merge, causing large areas of dead leaf tissue",
            "Severe infection causes premature leaf death and stalk lodging risk",
        ],
        "causes": [
            "Caused by the fungus Cercospora zeae-maydis",
            "Survives in corn residue left on the soil surface",
            "Spreads via windborne and rain-splashed spores",
            "Favoured by warm, humid weather and extended leaf wetness, common in no-till fields",
        ],
        "treatment": [
            "Apply foliar fungicides (strobilurin or triazole-based) at first sign of disease, especially before tasseling",
            "Time fungicide applications based on local disease pressure forecasts",
            "Monitor fields closely in continuous corn and no-till systems",
        ],
        "prevention": [
            "Rotate with non-host crops (soybeans, small grains) for at least one year",
            "Till under crop residue to speed decomposition where practical",
            "Plant resistant or tolerant hybrids",
            "Avoid excessive plant density which increases humidity within the canopy",
        ],
        "recommended_pesticides": [
            {
                "name": "Azoxystrobin",
                "type": "Strobilurin Fungicide",
                "usage": "Apply at VT (tasseling) stage per label for best yield protection",
            },
            {
                "name": "Propiconazole",
                "type": "Triazole Fungicide",
                "usage": "Apply at first symptom onset; rotate with other fungicide classes",
            },
        ],
        "severity": "High - can cause significant yield loss in susceptible hybrids under favourable conditions",
        "season": "Warm, humid weather mid-to-late in the growing season",
    },
    "Corn___Common_rust": {
        "disease_name": "Corn Common Rust",
        "scientific_name": "Puccinia sorghi",
        "description": "Common rust produces reddish-brown pustules on corn leaves. Most modern hybrids tolerate it well, but severe early infections can still reduce yield.",
        "symptoms": [
            "Small, circular to elongate reddish-brown pustules on both leaf surfaces",
            "Pustules rupture and release powdery, brick-red spores",
            "Pustules turn dark brown/black as the plant matures",
            "Heavily infected leaves may yellow and die prematurely",
        ],
        "causes": [
            "Caused by the fungus Puccinia sorghi",
            "Spores blow in from southern overwintering areas each season",
            "Favoured by cool temperatures (16-23°C) and high humidity/dew",
            "Does not survive winter in most temperate corn-growing regions",
        ],
        "treatment": [
            "Apply fungicides (strobilurin or triazole-based) if infection is severe before tasseling",
            "Most hybrids have adequate resistance and rarely need treatment",
            "Monitor susceptible sweet corn varieties more closely",
        ],
        "prevention": [
            "Plant rust-resistant hybrids, especially for sweet corn",
            "Scout fields regularly during cool, humid weather",
            "Avoid excessive nitrogen which can increase susceptibility",
        ],
        "recommended_pesticides": [
            {
                "name": "Azoxystrobin",
                "type": "Strobilurin Fungicide",
                "usage": "Apply only if disease is severe and hybrid is susceptible",
            },
            {
                "name": "Propiconazole",
                "type": "Triazole Fungicide",
                "usage": "Apply per label if pustule coverage exceeds economic threshold",
            },
        ],
        "severity": "Low to Moderate - most hybrids are resistant; sweet corn is more susceptible",
        "season": "Cool, humid weather; spores arrive via wind currents each growing season",
    },
    "Corn___Northern_Leaf_Blight": {
        "disease_name": "Corn Northern Leaf Blight",
        "scientific_name": "Exserohilum turcicum",
        "description": "Northern leaf blight causes large, cigar-shaped gray-green to tan lesions on corn leaves, capable of significantly reducing yield if it develops before or during grain fill.",
        "symptoms": [
            "Long, elliptical, cigar-shaped lesions 1-6 inches long",
            "Lesions are gray-green at first, turning tan to brown as they mature",
            "Lesions often start on lower leaves and progress upward",
            "Severe infections can cause a scorched, blighted appearance across the whole plant",
        ],
        "causes": [
            "Caused by the fungus Exserohilum turcicum",
            "Survives in corn residue on the soil surface",
            "Spreads via windborne and rain-splashed spores",
            "Favoured by moderate temperatures (18-27°C) and extended leaf wetness (dew, rain)",
        ],
        "treatment": [
            "Apply foliar fungicides (strobilurin/triazole combinations) at first symptom onset",
            "Prioritize fungicide use if disease appears before or at tasseling",
            "Scout continuous corn and no-till fields closely",
        ],
        "prevention": [
            "Plant resistant hybrids - a highly effective long-term strategy",
            "Rotate crops away from corn for at least one year",
            "Manage crop residue via tillage where appropriate",
            "Avoid irrigation practices that extend leaf wetness overnight",
        ],
        "recommended_pesticides": [
            {
                "name": "Azoxystrobin + Propiconazole",
                "type": "Combination Fungicide",
                "usage": "Apply at first lesion detection, especially pre-tassel",
            },
            {
                "name": "Pyraclostrobin",
                "type": "Strobilurin Fungicide",
                "usage": "Apply per label during early reproductive stages for best yield protection",
            },
        ],
        "severity": "High - can cause substantial yield loss if established before grain fill",
        "season": "Moderate temperatures with extended periods of leaf wetness, mid-season",
    },
    "Corn___healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your corn plant appears healthy! Here are some tips to maximize yield.",
        "symptoms": [
            "Leaves are uniformly green with no lesions, pustules, or blight",
            "Strong, upright stalks with no lodging",
            "Good ear development and kernel fill",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your plant looks healthy!",
            "Continue regular scouting, especially during humid mid-season weather",
        ],
        "prevention": [
            "Rotate crops to break disease cycles in residue",
            "Choose hybrids with strong disease resistance ratings for your region",
            "Manage crop residue appropriately for your tillage system",
            "Scout fields weekly from knee-high through grain fill",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Fertilize based on soil test and yield goals, split nitrogen applications",
            "Ensure adequate but not excessive plant population for your hybrid",
            "Monitor for corn borer, rootworm, and other key pests",
            "Scout for foliar disease onset especially in continuous corn fields",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
    # ------------------------------------------------------------------ #
    # Grape
    # ------------------------------------------------------------------ #
    "Grape___Black_rot": {
        "disease_name": "Grape Black Rot",
        "scientific_name": "Guignardia bidwellii",
        "description": "Black rot is one of the most destructive grape diseases in warm, humid climates, capable of destroying an entire crop by rotting berries before harvest if left unmanaged.",
        "symptoms": [
            "Small, reddish-brown circular spots on leaves with darker margins",
            "Black pycnidia (fungal fruiting bodies) visible within leaf spots",
            "Berries develop light brown spots that rapidly spread over the whole fruit",
            'Infected berries shrivel into hard, black "mummies"',
        ],
        "causes": [
            "Caused by the fungus Guignardia bidwellii",
            "Overwinters in mummified berries and infected canes left in the vineyard",
            "Spreads via rain-splashed spores in spring and early summer",
            "Favoured by warm, wet weather during bloom through berry development",
        ],
        "treatment": [
            "Apply fungicides (mancozeb, myclobutanil) starting at bud break and through veraison",
            "Remove and destroy mummified berries and infected canes during dormant pruning",
            "Maintain a strict spray schedule during the critical early season period",
        ],
        "prevention": [
            "Remove all mummified fruit from the vine and ground each dormant season",
            "Prune for an open canopy to speed drying after rain",
            "Choose less susceptible varieties where climate risk is high",
            "Avoid working in wet vineyards which can spread spores",
        ],
        "recommended_pesticides": [
            {
                "name": "Mancozeb",
                "type": "Protectant Fungicide",
                "usage": "Apply from bud break through bloom on a 7-14 day schedule",
            },
            {
                "name": "Myclobutanil",
                "type": "Systemic Fungicide",
                "usage": "Apply per label, especially during the 6-week post-bloom critical period",
            },
        ],
        "severity": "High - can destroy entire crop in warm, wet seasons if untreated",
        "season": "Warm, wet weather from bud break through berry development",
    },
    "Grape___Esca_Black_Measles": {
        "disease_name": "Grape Esca (Black Measles)",
        "scientific_name": "Phaeomoniella chlamydospora and associated fungi",
        "description": "Esca, also called Black Measles, is a complex trunk disease of grapevines caused by several wood-rotting fungi, leading to internal decay, leaf discoloration, and vine decline over years.",
        "symptoms": [
            '"Tiger-stripe" pattern of yellow/red discoloration between leaf veins',
            "Dark spots (measles) on berries with a purple-brown ring",
            "Sudden vine collapse (apoplexy) possible in hot weather",
            "Internal wood shows dark streaking or spongy decay when cut",
        ],
        "causes": [
            "Caused by a complex of fungi including Phaeomoniella chlamydospora and Phaeoacremonium species",
            "Enters through pruning wounds and other trunk injuries",
            "Develops slowly over multiple years inside the vine's woody tissue",
            "Favoured by older vines, large pruning wounds, and vine stress",
        ],
        "treatment": [
            "No effective chemical cure exists once established - management is preventive and cultural",
            "Prune out and destroy severely affected cordons or trunks",
            "Retrain new trunks from healthy suckers if the vine is valuable",
            "Protect fresh pruning wounds with a wound sealant or fungicide paste",
        ],
        "prevention": [
            "Prune during dry weather to reduce infection risk through wounds",
            "Make smaller, cleaner pruning cuts and avoid large wounds where possible",
            "Remove and destroy severely infected vines to reduce inoculum",
            "Avoid vine stress from drought or over-cropping",
        ],
        "recommended_pesticides": [
            {
                "name": "Wound sealant/fungicide paste",
                "type": "Protective Wound Treatment",
                "usage": "Apply immediately after pruning to reduce fungal entry, per product label",
            },
        ],
        "severity": "High - a chronic, largely incurable trunk disease that shortens vineyard productive life",
        "season": "Symptoms often appear/worsen during hot, dry summer weather; infection occurs at pruning time",
    },
    "Grape___Leaf_blight_Isariopsis": {
        "disease_name": "Grape Leaf Blight (Isariopsis Leaf Spot)",
        "scientific_name": "Pseudocercospora vitis (syn. Isariopsis clavispora)",
        "description": "Isariopsis leaf blight causes angular leaf spots that can lead to significant defoliation late in the season, weakening vines and reducing fruit ripening quality.",
        "symptoms": [
            "Small, angular, dark brown to black spots on leaves, bounded by veins",
            "Spots may merge into larger irregular blighted areas",
            "Yellowing of leaf tissue surrounding spots",
            "Premature defoliation in severe cases, starting with older leaves",
        ],
        "causes": [
            "Caused by the fungus Pseudocercospora vitis",
            "Overwinters in fallen leaf debris",
            "Spreads via rain-splashed and windborne spores",
            "Favoured by warm, humid weather, particularly later in the growing season",
        ],
        "treatment": [
            "Apply fungicides (mancozeb or copper-based products) if disease pressure is high",
            "Remove fallen leaf debris after harvest to reduce overwintering inoculum",
            "Improve canopy airflow through leaf pulling and proper training",
        ],
        "prevention": [
            "Maintain an open canopy through proper pruning and leaf removal",
            "Avoid excessive nitrogen fertilization that promotes dense canopies",
            "Rotate fungicide classes to prevent resistance development",
            "Remove and destroy fallen leaves each autumn",
        ],
        "recommended_pesticides": [
            {
                "name": "Mancozeb",
                "type": "Protectant Fungicide",
                "usage": "Apply on a preventive schedule during warm, humid periods",
            },
            {
                "name": "Copper-based fungicide",
                "type": "Fungicide (organic option)",
                "usage": "Apply preventively, especially in organic vineyards",
            },
        ],
        "severity": "Moderate - primarily a late-season concern that can weaken vines over time",
        "season": "Warm, humid weather in mid-to-late summer",
    },
    "Grape___healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your grapevine appears healthy! Here are some tips to keep it productive.",
        "symptoms": [
            "Leaves are uniformly green with no spots, blight, or discoloration",
            "No berry rot, shriveling, or unusual spotting",
            "Vigorous, well-trained canopy growth",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your vine looks healthy!",
            "Continue regular monitoring, especially during warm, humid weather",
        ],
        "prevention": [
            "Prune annually during dry weather for an open, airy canopy",
            "Remove mummified fruit and fallen leaves each dormant season",
            "Maintain a preventive fungicide program in high-disease-pressure regions",
            "Avoid vine stress from over-cropping or drought",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Train and trellis vines for good sun exposure and airflow",
            "Manage irrigation carefully - grapes prefer moderate, consistent moisture",
            "Thin fruit clusters if overloaded to improve ripening quality",
            "Monitor for key pests such as grape berry moth and Japanese beetle",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
    # ------------------------------------------------------------------ #
    # Orange
    # ------------------------------------------------------------------ #
    "Orange___Huanglongbing_Citrus_greening": {
        "disease_name": "Citrus Greening (Huanglongbing / HLB)",
        "scientific_name": "Candidatus Liberibacter spp.",
        "description": "Huanglongbing (HLB), or citrus greening, is one of the most destructive citrus diseases worldwide. It is spread by the Asian citrus psyllid and has no cure - infected trees decline and eventually die.",
        "symptoms": [
            "Asymmetric, blotchy yellow mottling on leaves (different on each side of the leaf)",
            "Small, misshapen, bitter-tasting fruit that stays partially green at the bottom",
            'Yellow shoots ("yellow dragon" appearance, the origin of the Chinese name)',
            "Twig dieback and progressive canopy thinning over time",
            "Premature fruit drop",
        ],
        "causes": [
            "Caused by the bacteria Candidatus Liberibacter asiaticus/africanus/americanus",
            "Transmitted by the Asian citrus psyllid (Diaphorina citri) as it feeds",
            "Can also spread via grafting infected budwood",
            "No known cure once a tree is infected",
        ],
        "treatment": [
            "There is no cure - focus is on psyllid control and removing infected trees",
            "Apply systemic insecticides to control the Asian citrus psyllid vector",
            "Remove and destroy confirmed infected trees to reduce disease spread",
            "Support tree health with balanced nutrition to slow decline (does not cure disease)",
        ],
        "prevention": [
            "Plant only certified disease-free nursery stock",
            "Monitor and control Asian citrus psyllid populations aggressively",
            "Inspect trees regularly for early mottling symptoms",
            "Remove and destroy infected trees immediately to protect neighboring trees",
            "Coordinate area-wide psyllid management with neighboring growers",
        ],
        "recommended_pesticides": [
            {
                "name": "Imidacloprid",
                "type": "Systemic Insecticide (for psyllid vector)",
                "usage": "Apply as a soil drench per label to control psyllid populations",
            },
            {
                "name": "Foliar insecticides (various)",
                "type": "Insecticide (for psyllid vector)",
                "usage": "Rotate modes of action per local extension guidance to manage psyllids",
            },
        ],
        "severity": "Very High - incurable, ultimately fatal to the tree, and a major economic threat to citrus production",
        "season": "Year-round risk wherever the Asian citrus psyllid is present",
    },
    # ------------------------------------------------------------------ #
    # Peach
    # ------------------------------------------------------------------ #
    "Peach___Bacterial_spot": {
        "disease_name": "Peach Bacterial Spot",
        "scientific_name": "Xanthomonas arboricola pv. pruni",
        "description": "Bacterial spot is a major disease of peaches and other stone fruit, causing leaf spots, defoliation, and unsightly fruit lesions that reduce marketable yield, especially in wet regions.",
        "symptoms": [
            "Small, angular, water-soaked spots on leaves that turn purple to brown",
            'Leaf centers can dry out and fall away, giving a "shot-hole" appearance',
            "Dark, sunken, scabby lesions on fruit surface, sometimes cracking",
            "Premature leaf yellowing and drop in severe cases",
        ],
        "causes": [
            "Caused by the bacterium Xanthomonas arboricola pv. pruni",
            "Spreads via wind-driven rain and overhead irrigation",
            "Enters through natural openings and wounds",
            "Favoured by warm, wet weather and sandy soils with low nutrient buffering",
        ],
        "treatment": [
            "Apply copper-based bactericides during dormant season and early growing season",
            "Avoid excessive nitrogen fertilization which increases susceptibility",
            "Prune to improve air circulation and speed leaf drying",
        ],
        "prevention": [
            "Plant resistant peach varieties where available",
            "Avoid overhead irrigation - use drip irrigation instead",
            "Apply preventive copper sprays before bud break in high-risk orchards",
            "Avoid planting in poorly drained, sandy soils prone to nutrient stress",
        ],
        "recommended_pesticides": [
            {
                "name": "Copper Hydroxide",
                "type": "Bactericide",
                "usage": "Apply during dormancy and again at early leaf emergence per label",
            },
            {
                "name": "Oxytetracycline",
                "type": "Bactericide (where permitted)",
                "usage": "Use only where locally approved, following label rates strictly",
            },
        ],
        "severity": "Moderate to High - can significantly reduce fruit quality and cause defoliation in wet years",
        "season": "Warm, wet spring and early summer weather",
    },
    "Peach___healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your peach tree appears healthy! Here are some tips to keep it productive.",
        "symptoms": [
            "Leaves are uniformly green with no spotting or shot-holes",
            "No fruit lesions, cracking, or premature drop",
            "Healthy bark with no cankers or gumming",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your tree looks healthy!",
            "Continue regular monitoring, especially during wet spring weather",
        ],
        "prevention": [
            "Prune annually for an open canopy and good airflow",
            "Water at the base, avoiding wetting foliage",
            "Apply a dormant-season copper spray in disease-prone regions",
            "Maintain balanced fertility - avoid excess nitrogen",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Thin fruit early to improve size and reduce limb stress",
            "Fertilize based on soil test results",
            "Monitor for peach leaf curl, brown rot, and borers regularly",
            "Water deeply during dry spells, especially during fruit development",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
    # ------------------------------------------------------------------ #
    # Raspberry
    # ------------------------------------------------------------------ #
    "Raspberry___healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your raspberry plant appears healthy! Here are some tips to keep it productive.",
        "symptoms": [
            "Canes are green/healthy-colored with no cankers or spotting",
            "Leaves are uniformly green with no spots or yellowing",
            "Good fruit set and cane vigor",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your plant looks healthy!",
            "Continue regular monitoring for cane diseases and pests",
        ],
        "prevention": [
            "Prune out old fruiting canes after harvest to improve airflow",
            "Space canes properly to reduce humidity within the row",
            "Avoid overhead irrigation late in the day",
            "Remove wild/volunteer brambles nearby that can harbor disease",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Trellis canes to keep fruit off the ground and improve airflow",
            "Mulch to conserve moisture and suppress weeds",
            "Fertilize lightly in spring - raspberries dislike excess nitrogen",
            "Monitor for spotted wing drosophila during fruiting",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
    # ------------------------------------------------------------------ #
    # Soybean
    # ------------------------------------------------------------------ #
    "Soybean___healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your soybean plant appears healthy! Here are some tips to maximize yield.",
        "symptoms": [
            "Leaves are uniformly green with no spots, mosaic, or yellowing",
            "Good pod set with no premature leaf drop",
            "Vigorous, well-nodulated root system",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your plant looks healthy!",
            "Continue regular scouting throughout the growing season",
        ],
        "prevention": [
            "Rotate with non-host crops such as corn to break disease cycles",
            "Choose varieties with strong local disease resistance ratings",
            "Manage field drainage - many soybean diseases favour wet soils",
            "Scout weekly from emergence through pod fill",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Ensure proper inoculation with Bradyrhizobium japonicum at planting for nitrogen fixation",
            "Manage weeds early - competition significantly reduces yield",
            "Monitor for soybean aphid, cyst nematode, and foliar disease pressure",
            "Fertilize based on soil test - soybeans usually need little added nitrogen",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
    # ------------------------------------------------------------------ #
    # Squash
    # ------------------------------------------------------------------ #
    "Squash___Powdery_mildew": {
        "disease_name": "Squash Powdery Mildew",
        "scientific_name": "Podosphaera xanthii (syn. Erysiphe cichoracearum)",
        "description": "Powdery mildew is the most common disease of squash and other cucurbits, coating leaves and stems in white powdery fungal growth that reduces photosynthesis and weakens the plant.",
        "symptoms": [
            "White, powdery circular spots on upper and lower leaf surfaces",
            "Spots enlarge and merge until the whole leaf appears dusted with powder",
            "Infected leaves yellow, curl, and die prematurely",
            "Reduced fruit size, quality, and sugar content in severe infections",
        ],
        "causes": [
            "Caused by fungi including Podosphaera xanthii",
            "Spreads via windborne spores, does not require free water to infect",
            "Favoured by warm days, high humidity, and shaded/crowded plantings",
            "Can develop rapidly, especially late in the growing season",
        ],
        "treatment": [
            "Apply fungicides (sulfur, potassium bicarbonate, or myclobutanil) at first sign of white spots",
            "Remove and destroy heavily infected leaves",
            "Improve air circulation by proper plant spacing and pruning",
            "Repeat treatments per label as new growth emerges",
        ],
        "prevention": [
            "Plant resistant/tolerant squash varieties where available",
            "Space plants properly for good airflow",
            "Avoid excess nitrogen fertilization which promotes susceptible new growth",
            "Water at the base and avoid wetting foliage",
        ],
        "recommended_pesticides": [
            {
                "name": "Sulfur",
                "type": "Fungicide (organic option)",
                "usage": "Apply at first sign of disease; avoid during high heat to prevent leaf burn",
            },
            {
                "name": "Potassium bicarbonate",
                "type": "Fungicide (organic option)",
                "usage": "Contact fungicide, apply every 7-14 days",
            },
            {
                "name": "Myclobutanil",
                "type": "Systemic Fungicide",
                "usage": "Apply per label, rotate fungicide classes to avoid resistance",
            },
        ],
        "severity": "Moderate to High - can significantly reduce yield and vine vigor if untreated",
        "season": "Warm, humid weather; often worsens in mid-to-late summer",
    },
    # ------------------------------------------------------------------ #
    # Strawberry
    # ------------------------------------------------------------------ #
    "Strawberry___Leaf_scorch": {
        "disease_name": "Strawberry Leaf Scorch",
        "scientific_name": "Diplocarpon earlianum",
        "description": "Leaf scorch is a common fungal disease of strawberries that causes numerous small purple spots on leaves, which can merge into large scorched-looking blotches and weaken the plant.",
        "symptoms": [
            "Small, irregular purple to red spots scattered across leaf surface",
            "Spots lack the tan/gray center typical of leaf spot disease",
            "Spots merge into larger blotches, giving leaves a scorched appearance",
            "Severe infection reduces plant vigor and fruit yield",
        ],
        "causes": [
            "Caused by the fungus Diplocarpon earlianum",
            "Overwinters on infected leaf debris",
            "Spreads via rain-splashed spores",
            "Favoured by warm, wet weather and dense, poorly ventilated plantings",
        ],
        "treatment": [
            "Apply fungicides (captan or myclobutanil) at first sign of symptoms",
            "Remove and destroy severely infected leaves after harvest (renovation)",
            "Improve air circulation through proper plant spacing",
        ],
        "prevention": [
            "Plant resistant strawberry varieties where available",
            "Space plants for good airflow and avoid overcrowded beds",
            "Remove old/infected leaves during post-harvest renovation",
            "Avoid overhead irrigation late in the day",
        ],
        "recommended_pesticides": [
            {
                "name": "Captan",
                "type": "Fungicide",
                "usage": "Apply as a protectant spray every 7-14 days during wet weather",
            },
            {
                "name": "Myclobutanil",
                "type": "Systemic Fungicide",
                "usage": "Apply per label at first symptom onset",
            },
        ],
        "severity": "Moderate - reduces plant vigor and yield but rarely kills the plant",
        "season": "Warm, wet weather; often worst in spring and after fruiting",
    },
    "Strawberry___healthy": {
        "disease_name": "Healthy Plant",
        "scientific_name": "N/A",
        "description": "Your strawberry plant appears healthy! Here are some tips to keep it productive.",
        "symptoms": [
            "Leaves are uniformly green with no spotting or scorching",
            "No wilting, root rot, or fruit lesions",
            "Vigorous runners and good fruit set",
        ],
        "causes": [],
        "treatment": [
            "No treatment needed - your plant looks healthy!",
            "Continue regular monitoring for pests and early disease signs",
        ],
        "prevention": [
            "Renovate beds after harvest - remove old leaves and thin runners",
            "Space plants for good airflow",
            "Use mulch (straw) to keep fruit off the soil and reduce splash",
            "Rotate planting beds every few years to avoid soil-borne disease buildup",
        ],
        "recommended_pesticides": [],
        "care_tips": [
            "Water consistently, especially during flowering and fruiting",
            "Fertilize lightly - excess nitrogen promotes leaves over fruit",
            "Protect ripening fruit from slugs and birds",
            "Monitor for gray mold (Botrytis) during wet fruiting periods",
        ],
        "severity": "None - Plant is healthy!",
        "season": "N/A",
    },
}


def get_disease_context(disease_class: str) -> str:
    """Generate a comprehensive context string for the RAG chatbot."""
    info = PLANT_DISEASE_KNOWLEDGE.get(disease_class)
    if not info:
        return "No information available for this classification."

    context_parts = [
        f"## Disease Detected: {info['disease_name']}",
        f"**Scientific Name:** {info.get('scientific_name', 'N/A')}",
        f"\n**Description:** {info['description']}",
    ]

    if info.get("symptoms"):
        context_parts.append("\n**Symptoms:**")
        for s in info["symptoms"]:
            context_parts.append(f"- {s}")

    if info.get("causes"):
        context_parts.append("\n**Causes:**")
        for c in info["causes"]:
            context_parts.append(f"- {c}")

    if info.get("treatment"):
        context_parts.append("\n**Treatment:**")
        for t in info["treatment"]:
            context_parts.append(f"- {t}")

    if info.get("prevention"):
        context_parts.append("\n**Prevention:**")
        for p in info["prevention"]:
            context_parts.append(f"- {p}")

    if info.get("recommended_pesticides"):
        context_parts.append("\n**Recommended Pesticides/Fungicides:**")
        for pest in info["recommended_pesticides"]:
            context_parts.append(f"- **{pest['name']}** ({pest['type']}): {pest['usage']}")

    if info.get("care_tips"):
        context_parts.append("\n**Care Tips:**")
        for tip in info["care_tips"]:
            context_parts.append(f"- {tip}")

    context_parts.append(f"\n**Severity:** {info.get('severity', 'Unknown')}")
    context_parts.append(f"**Season:** {info.get('season', 'Unknown')}")

    return "\n".join(context_parts)
