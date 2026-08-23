# Business Verticals
BUSINESSES = [
    {
        'id': 'plumbing',
        'name': 'Plumbing and Industrial materials',
        'slug': 'plumbing',
        'short_description': 'Pipes, fittings, valves, pumps, and water management solutions from top brands.',
        'icon': '🔧',
        'order': 1
    },
    {
        'id': 'hardware',
        'name': 'Paints,Hardwares and doorfittings',
        'slug': 'hardware',
        'short_description': 'Door fittings, fasteners, tools, safety equipment, and industrial hardware.',
        'icon': '🔨',
        'order': 2
    },
    {
        'id': 'bath-kitchen',
        'name': 'Bath and sanitaryware',
        'slug': 'bath-kitchen',
        'short_description': 'Sanitaryware, faucets, showers, bathtubs, kitchen sinks, and accessories.',
        'icon': '🛁',
        'order': 3
    },
    {
        'id': 'catalogue',
        'name': 'Product Catalogue',
        'slug': 'catalogue',
        'short_description': 'General catalogue items and miscellaneous materials.',
        'icon': '📦',
        'order': 4
    }
]

# Authorized Brands (All official dealers & suppliers for Sathik Traders)
BRANDS_LIST = [
    {'name': 'Jaquar', 'slug': 'jaquar', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'Hindware', 'slug': 'hindware', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'C.R.I. Pumps', 'slug': 'cri', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'EKKI Water Tech', 'slug': 'ekki', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'ÉSSCO Bath Fittings', 'slug': 'eesco', 'businesses': ['bath-kitchen', 'plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Parryware', 'slug': 'parryware', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'Geberit', 'slug': 'geberit', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'Switzerland'},
    {'name': 'Grohe', 'slug': 'grohe', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'Germany'},
    {'name': 'Aqua Tech Tanks', 'slug': 'aquatech', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Waterman', 'slug': 'waterman', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'Waterstar', 'slug': 'waterstar', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'G-Bath', 'slug': 'g-bath', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'Germa', 'slug': 'germa', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'Kreesta', 'slug': 'kreesta', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'Benicio', 'slug': 'benicio', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'Clayware', 'slug': 'clayware', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
    {'name': 'Rasi', 'slug': 'rasi', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Best Arc', 'slug': 'best-arc', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Supron', 'slug': 'supron', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Alpha', 'slug': 'alpha', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Bosch', 'slug': 'bosch', 'businesses': ['plumbing'], 'featured': True, 'country': 'Germany'},
    {'name': 'DeWalt', 'slug': 'dewalt', 'businesses': ['plumbing'], 'featured': True, 'country': 'USA'},
    {'name': 'Polymach', 'slug': 'polymach', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Valley Wolf', 'slug': 'valley-wolf', 'businesses': ['plumbing'], 'featured': True, 'country': 'China'},
    {'name': 'Taparia', 'slug': 'taparia', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Legrand', 'slug': 'legrand', 'businesses': ['plumbing'], 'featured': True, 'country': 'France'},
    {'name': 'GB Company', 'slug': 'gb-company', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Roma', 'slug': 'roma', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Oswin', 'slug': 'oswin', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Finolex', 'slug': 'finolex', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Orbit', 'slug': 'orbit', 'businesses': ['plumbing'], 'featured': True, 'country': 'India'},
    {'name': 'Orca', 'slug': 'orca', 'businesses': ['bath-kitchen'], 'featured': True, 'country': 'India'},
]

# Official Sathik Traders Contact & Location Info
COMPANY_INFO = {
    'name': 'Sathik Traders',
    'full_name': 'Sathik Traders (Sathik Groups)',
    'phone': '044-26322644',
    'mobile': '94443 23644',
    'mobile_formatted': '+91 94443 23644',
    'whatsapp': '919444323644',
    'email': 'sathiktradersredhills@gmail.com',
    'email_alt': 'sathik_traders@yahoo.co.in',
    'address': 'No.6, Dharga Street, G.N.T. Road, Redhills, Chennai - 600 052',
    'street': 'No.6, Dharga Street, G.N.T. Road',
    'area': 'Redhills',
    'city': 'Chennai',
    'state': 'Tamil Nadu',
    'pincode': '600 052',
    'website': 'www.sathiktraders.com',
    'hours': 'Mon – Sat, 9:00 AM – 7:30 PM'
}

# MOCK CATEGORIES & SUBCATEGORIES FOR CLIENT PREVIEW
MOCK_CATEGORIES = [
    # Bath & Kitchen Store Categories
    {
        'name': 'Bathware',
        'slug': 'bathware',
        'business_slug': 'bath-kitchen',
        'description': 'Taps, shower systems, sanitary fixtures, lighting, geysers, bathtubs, and bathroom accessories.',
        'icon': '🛁',
        'order': 1
    },
    {
        'name': 'Kitchenware',
        'slug': 'kitchenware',
        'business_slug': 'bath-kitchen',
        'description': 'Stainless steel sinks, kitchen taps, chimneys, hobs, modular baskets, and drain racks.',
        'icon': '🍳',
        'order': 2
    },
    {
        'name': 'Bathroom Hardware & Mirrors',
        'slug': 'bath-hardware-mirrors',
        'business_slug': 'bath-kitchen',
        'description': 'LED touch mirrors, glass partition fittings, soap dispensers, and premium brass accessories.',
        'icon': '🪞',
        'order': 3
    },

    # Plumbing Products Store Categories
    {
        'name': 'Pipes & Tubing',
        'slug': 'pipes',
        'business_slug': 'plumbing',
        'description': 'CPVC, UPVC, SWR, and underground agricultural water pipes.',
        'icon': '🚰',
        'order': 1
    },
    {
        'name': 'Pipe Fittings & Valves',
        'slug': 'pipe-fittings',
        'business_slug': 'plumbing',
        'description': 'Elbows, tees, couplings, ball valves, gate valves, and brass joints.',
        'icon': '🔧',
        'order': 2
    },
    {
        'name': 'Pumps & Motors',
        'slug': 'pumps',
        'business_slug': 'plumbing',
        'description': 'Submersible pumps, monoblock pumps, and automated pressure booster systems.',
        'icon': '⚡',
        'order': 3
    },

    # Hardware Products Store Categories
    {
        'name': 'Paints & Building Chemistry',
        'slug': 'paints-chemicals',
        'business_slug': 'hardware',
        'description': 'Premium wall paints, white cement, waterproofing chemicals, and structural adhesives.',
        'icon': '🎨',
        'order': 1
    },
    {
        'name': 'Hardwares & Door Fittings',
        'slug': 'door-hardware',
        'business_slug': 'hardware',
        'description': 'Premium door locks, hinges, tower bolts, altraps, and tile fitting spacer accessories.',
        'icon': '🔑',
        'order': 2
    },
    {
        'name': 'Electrical & Fans',
        'slug': 'electrical-fans',
        'business_slug': 'hardware',
        'description': 'Energy-efficient ceiling and exhaust fans, and premium indoor/outdoor LED lights.',
        'icon': '⚡',
        'order': 3
    }
]

MOCK_SUBCATEGORIES = [
    # Bathware Elements
    {'name': 'Taps & Faucets', 'slug': 'taps-faucets', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '🚰', 'order': 1},
    {'name': 'Towel Rods & Hooks', 'slug': 'towel-rods-accessories', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '🧣', 'order': 2},
    {'name': 'Bathroom Lighting', 'slug': 'bathroom-lighting', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '💡', 'order': 3},
    {'name': 'Water Heaters & Geysers', 'slug': 'water-heaters-geysers', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '🔥', 'order': 4},
    {'name': 'Sanitaryware (Closets & Basins)', 'slug': 'sanitaryware-fixtures', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '🚽', 'order': 5},
    {'name': 'Showers & Enclosures', 'slug': 'showers-enclosures', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '🚿', 'order': 6},
    {'name': 'Bathtubs & Jacuzzis', 'slug': 'bathtubs', 'category_slug': 'bathware', 'business_slug': 'bath-kitchen', 'icon': '🛁', 'order': 7},

    # Kitchenware Elements
    {'name': 'Kitchen Sinks & Taps', 'slug': 'kitchen-sinks-taps', 'category_slug': 'kitchenware', 'business_slug': 'bath-kitchen', 'icon': '🚰', 'order': 1},
    {'name': 'Modular Kitchen Baskets', 'slug': 'kitchen-baskets', 'category_slug': 'kitchenware', 'business_slug': 'bath-kitchen', 'icon': '🗄️', 'order': 2},
    {'name': 'Kitchen Chimneys & Hobs', 'slug': 'chimneys-hobs', 'category_slug': 'kitchenware', 'business_slug': 'bath-kitchen', 'icon': '💨', 'order': 3},
    {'name': 'Drain Racks & Accessories', 'slug': 'drain-racks', 'category_slug': 'kitchenware', 'business_slug': 'bath-kitchen', 'icon': '🍽️', 'order': 4},

    # Bath Hardware & Mirrors Elements
    {'name': 'LED Touch Mirrors', 'slug': 'led-mirrors', 'category_slug': 'bath-hardware-mirrors', 'business_slug': 'bath-kitchen', 'icon': '🪞', 'order': 1},
    {'name': 'Soap Dispensers & Holders', 'slug': 'soap-dispensers', 'category_slug': 'bath-hardware-mirrors', 'business_slug': 'bath-kitchen', 'icon': '🧴', 'order': 2},
    {'name': 'Glass Partition Fittings', 'slug': 'shower-partitions', 'category_slug': 'bath-hardware-mirrors', 'business_slug': 'bath-kitchen', 'icon': '🚪', 'order': 3},

    # Plumbing Elements
    {'name': 'Pneumatic Fittings', 'slug': 'pneumatic-fittings', 'category_slug': 'pipe-fittings', 'business_slug': 'plumbing', 'icon': '💨', 'order': 1},
    {'name': 'Welding Equipment', 'slug': 'welding-equipment', 'category_slug': 'pipe-fittings', 'business_slug': 'plumbing', 'icon': '⚡', 'order': 2},
    {'name': 'Hoses & Suction Tubes', 'slug': 'hoses-tubes', 'category_slug': 'pipes', 'business_slug': 'plumbing', 'icon': '🌀', 'order': 3},
    {'name': 'Bolts & Nuts', 'slug': 'bolts-nuts', 'category_slug': 'pipe-fittings', 'business_slug': 'plumbing', 'icon': '🔩', 'order': 4},
    {'name': 'Pipeline Clamps', 'slug': 'pipeline-clamps', 'category_slug': 'pipe-fittings', 'business_slug': 'plumbing', 'icon': '🧲', 'order': 5},
    {'name': 'Submersible Pumps', 'slug': 'submersible-pumps', 'category_slug': 'pumps', 'business_slug': 'plumbing', 'icon': '⛲', 'order': 6},
    {'name': 'Power Tools', 'slug': 'power-tools', 'category_slug': 'pumps', 'business_slug': 'plumbing', 'icon': '⚙️', 'order': 7},
    {'name': 'Engineering Tools', 'slug': 'engineering-tools', 'category_slug': 'pumps', 'business_slug': 'plumbing', 'icon': '🛠️', 'order': 8},
    {'name': 'Tap Spindles', 'slug': 'tap-spindles', 'category_slug': 'pipe-fittings', 'business_slug': 'plumbing', 'icon': '🚰', 'order': 9},
    {'name': 'Electrical Switches', 'slug': 'electrical-switches', 'category_slug': 'pipe-fittings', 'business_slug': 'plumbing', 'icon': '🔌', 'order': 10},
    {'name': 'MCB & Protection', 'slug': 'electrical-mcb', 'category_slug': 'pipe-fittings', 'business_slug': 'plumbing', 'icon': '📟', 'order': 11},
    {'name': 'Electrical Wires', 'slug': 'electrical-wires', 'category_slug': 'pipes', 'business_slug': 'plumbing', 'icon': '〰️', 'order': 12},

    # Hardware Elements
    {'name': 'Paints', 'slug': 'paints', 'category_slug': 'paints-chemicals', 'business_slug': 'hardware', 'icon': '🎨', 'order': 1},
    {'name': 'White Cement', 'slug': 'white-cement', 'category_slug': 'paints-chemicals', 'business_slug': 'hardware', 'icon': '🧱', 'order': 2},
    {'name': 'Water Proofing Chemicals', 'slug': 'waterproofing-chemicals', 'category_slug': 'paints-chemicals', 'business_slug': 'hardware', 'icon': '💧', 'order': 3},
    {'name': 'Adhesives', 'slug': 'adhesives', 'category_slug': 'paints-chemicals', 'business_slug': 'hardware', 'icon': '🧪', 'order': 4},
    {'name': 'Locks', 'slug': 'locks', 'category_slug': 'door-hardware', 'business_slug': 'hardware', 'icon': '🔒', 'order': 5},
    {'name': 'Hinges', 'slug': 'hinges', 'category_slug': 'door-hardware', 'business_slug': 'hardware', 'icon': '🚪', 'order': 6},
    {'name': 'Tower Bolts', 'slug': 'tower-bolts', 'category_slug': 'door-hardware', 'business_slug': 'hardware', 'icon': '🔩', 'order': 7},
    {'name': 'Altraps', 'slug': 'altraps', 'category_slug': 'door-hardware', 'business_slug': 'hardware', 'icon': '⛓️', 'order': 8},
    {'name': 'Tile Beeding and Paser', 'slug': 'tile-beeding-paser', 'category_slug': 'door-hardware', 'business_slug': 'hardware', 'icon': '📐', 'order': 9},
    {'name': 'Fans', 'slug': 'fans', 'category_slug': 'electrical-fans', 'business_slug': 'hardware', 'icon': '🌀', 'order': 10},
    {'name': 'LED Lights', 'slug': 'led-lights', 'category_slug': 'electrical-fans', 'business_slug': 'hardware', 'icon': '💡', 'order': 11}
]

# MOCK SAMPLE PRODUCTS FOR CLIENT PREVIEW
MOCK_PRODUCTS = [
    # --- BATH & KITCHEN: NEW PRODUCTS ---
    {
        '_id': 'p_bath_water_heater',
        'name': 'Hindware Elena Storage Water Heater 25L',
        'slug': 'hindware-elena-storage-water-heater-25l',
        'sku': 'HIND-GYS-25L',
        'description': 'Energy-efficient 5-star rated storage geyser with glass-lined tank, titanium heating element, and multi-tier safety valve for instant hot water.',
        'short_description': '25-Liter 5-star energy-efficient electric water heater.',
        'features': ['Titanium glass-lined tank', '5-Star BEE energy rating', 'High pressure withstand up to 8 Bar'],
        'specifications': [{'key': 'Capacity', 'value': '25 Liters'}, {'key': 'Rating', 'value': '5 Star BEE'}],
        'images': [{'url': '/static/images/products/bath-kitchen/water_heater.jpg', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'bathware',
        'subcategory_slug': 'water-heaters-geysers',
        'brand_slug': 'hindware',
        'brand_name': 'Hindware',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_bath_ss_sink',
        'name': 'Stainless Steel Kitchen Sink',
        'slug': 'stainless-steel-kitchen-sink',
        'sku': 'CERA-SNK-SS',
        'description': 'Premium double bowl kitchen sink constructed from grade 304 satin-finished stainless steel with anti-noise rubber dampening pads.',
        'short_description': 'Grade 304 satin finish double bowl stainless steel kitchen sink.',
        'features': ['Heavy duty 1.2mm SS 304 steel', 'Undercoated sound deadening pads', 'Includes waste coupling strainers'],
        'specifications': [{'key': 'Material', 'value': 'SS 304 Satin'}],
        'images': [{'url': '/static/images/products/bath-kitchen/stainless_sink.jpg', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'kitchenware',
        'subcategory_slug': 'kitchen-sinks-taps',
        'brand_slug': 'cera',
        'brand_name': 'CERA',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_bath_quartz_sink',
        'name': 'Quartz Kitchen Sink',
        'slug': 'quartz-kitchen-sink',
        'sku': 'CERA-SNK-QZ',
        'description': 'Luxurious composite double bowl kitchen sink with scratch-resistant, heat-resistant, and germ-block surface technology.',
        'short_description': 'Luxurious black quartz double bowl kitchen sink.',
        'features': ['Composite quartz granite material', 'Heat and scratch resistant', 'Hygienic easy-to-clean design'],
        'specifications': [{'key': 'Material', 'value': 'Quartz Granite'}],
        'images': [{'url': '/static/images/products/bath-kitchen/quartz_sink.jpg', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'kitchenware',
        'subcategory_slug': 'kitchen-sinks-taps',
        'brand_slug': 'cera',
        'brand_name': 'CERA',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_bath_bathtub_orca',
        'name': 'Orca Acrylic Freestanding Bathtub',
        'slug': 'orca-acrylic-freestanding-bathtub',
        'sku': 'ORCA-BT-01',
        'description': 'Orca premium freestanding white acrylic bathtub. Ergonomically contoured design with heavy-duty structural frame and sleek overflow system.',
        'short_description': 'Luxurious freestanding white acrylic bathtub by Orca.',
        'features': ['High-gloss lucite acrylic', 'Heavy steel support frame', 'Integrated overflow & drain'],
        'specifications': [{'key': 'Material', 'value': 'Acrylic'}, {'key': 'Brand', 'value': 'Orca'}],
        'images': [{'url': '/static/images/products/bath-kitchen/orca_bathtub.jpg', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'bathware',
        'subcategory_slug': 'bathtubs',
        'brand_slug': 'orca',
        'brand_name': 'Orca',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_bath_diverter',
        'name': 'Jaquar Kubix Prime Shower Diverter',
        'slug': 'jaquar-kubix-prime-shower-diverter',
        'sku': 'JAG-DIV-001',
        'description': 'Jaquar Kubix Prime high-flow single lever bathroom shower diverter with premium chrome plating and smooth ceramic cartridge.',
        'short_description': 'Premium single lever high-flow shower diverter.',
        'features': ['High flow cartridge', 'Mirror shine chrome finish', '10-Year manufacturer warranty'],
        'specifications': [{'key': 'Material', 'value': 'Brass'}, {'key': 'Finish', 'value': 'Chrome'}],
        'images': [{'url': '/static/images/products/bath-kitchen/diverter.jpg', 'is_primary': True}],
        'business_slug': 'bath-kitchen',
        'category_slug': 'bathware',
        'subcategory_slug': 'taps-faucets',
        'brand_slug': 'jaquar',
        'brand_name': 'Jaquar',
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },

    # --- PLUMBING STORE PRODUCTS ---
    {
        '_id': 'p_pneumatic_1',
        'name': 'Pneumatic Fittings',
        'slug': 'pneumatic-fittings',
        'sku': 'IND-PNE-001',
        'description': 'Premium industrial pneumatic fittings designed for high-pressure air systems, pneumatic tools, and automation equipment. Easy push-to-connect mechanism.',
        'short_description': 'Industrial grade push-to-connect pneumatic fittings.',
        'features': ['High working pressure tolerance', 'Push-to-connect quick installation', 'Corrosion-resistant nickel-plated brass body'],
        'specifications': [{'key': 'Material', 'value': 'Nickel-Plated Brass'}, {'key': 'Fitting Type', 'value': 'Push-in / Threaded'}],
        'images': [{'url': '/static/images/products/plumbing/pneumatic-fitting-products.jpg', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipe-fittings',
        'subcategory_slug': 'pneumatic-fittings',
        'brand_slug': 'standard',
        'brand_name': 'Standard',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_welding_rods',
        'name': 'Welding Rods',
        'slug': 'welding-rods',
        'sku': 'IND-WLD-RODS',
        'description': 'General-purpose and mild steel welding electrodes for structural fabrication. Choose from premium brands below.',
        'short_description': 'Mild steel welding electrodes from premium brands.',
        'features': ['Stable arc characteristics', 'Minimal spatter', 'Easy slag detachability'],
        'specifications': [{'key': 'Product Type', 'value': 'Welding Electrodes'}],
        'images': [{'url': '/static/images/products/plumbing/welding_rods.jpg', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipe-fittings',
        'subcategory_slug': 'welding-equipment',
        'brand_slug': 'multiple',
        'brand_name': 'Rasi / Best Arc / Supron',
        'available_brands': [
            {
                'brand_name': 'Rasi',
                'name': 'Rasi welding Rods',
                'sku': 'IND-WLD-RASI',
                'image': '/static/images/products/plumbing/rasi_welding_rods.jpg'
            },
            {
                'brand_name': 'Best Arc',
                'name': 'Best Arc welding rods',
                'sku': 'IND-WLD-BARC',
                'image': '/static/images/products/plumbing/best_arc_welding_rods.jpeg'
            },
            {
                'brand_name': 'Supron',
                'name': 'Supron Welding Rod',
                'sku': 'IND-WLD-SUPRON',
                'image': '/static/images/products/plumbing/supron_welding_rod.jpg'
            }
        ],
        'available_brand_slugs': ['rasi', 'best-arc', 'supron'],
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_welding_machine',
        'name': 'GB Company Welding Machine',
        'slug': 'gb-company-welding-machine',
        'sku': 'IND-WLD-GBMACH',
        'description': 'GB Company heavy-duty inverter welding machine. Compact design, high energy efficiency, and thermal protection for stable arc performance.',
        'short_description': 'Heavy duty inverter arc welding machine from GB Company.',
        'features': ['IGBT Inverter technology', 'Digital current display', 'Thermal overload protection'],
        'specifications': [{'key': 'Brand', 'value': 'GB Company'}, {'key': 'Current Range', 'value': '20-200A'}],
        'images': [{'url': '/static/images/products/plumbing/gb_company_welding_machine.jpg', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipe-fittings',
        'subcategory_slug': 'welding-equipment',
        'brand_slug': 'gb-company',
        'brand_name': 'GB Company',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_hose_alpha',
        'name': 'Alpha Suction Hose',
        'slug': 'alpha-suction-hose',
        'sku': 'IND-HSE-ALPHA',
        'description': 'Alpha brand heavy-duty reinforced spiral PVC suction hose. Excellent resistance to pressure, vacuum, chemicals, and weather.',
        'short_description': 'Spiral-reinforced PVC suction hose from Alpha.',
        'features': ['Reinforced rigid PVC spiral helix', 'Smooth inner bore for flow efficiency', 'Crush & weather resistant'],
        'specifications': [{'key': 'Brand', 'value': 'Alpha'}, {'key': 'Working Temp', 'value': '-10°C to +60°C'}],
        'images': [{'url': '/static/images/products/plumbing/suction_hose.webp', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipes',
        'subcategory_slug': 'hoses-tubes',
        'brand_slug': 'alpha',
        'brand_name': 'Alpha',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_hose_normal',
        'name': 'Flexible PVC Water Hose',
        'slug': 'flexible-pvc-water-hose',
        'sku': 'IND-HSE-NORMAL',
        'description': 'Flexible multi-layered braided PVC water hose for general garden watering, site cleaning, and industrial washing.',
        'short_description': 'Standard braided PVC water utility hose.',
        'features': ['High flexibility & kink resistance', 'Braided fiber reinforcement', 'Standard 1/2 inch and 3/4 inch sizes'],
        'specifications': [{'key': 'Material', 'value': 'Braided PVC'}, {'key': 'Reinforcement', 'value': 'Polyester Yarn'}],
        'images': [{'url': '/static/images/products/plumbing/normal_hose.png', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipes',
        'subcategory_slug': 'hoses-tubes',
        'brand_slug': 'standard',
        'brand_name': 'Standard',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': False,
        'is_new': False
    },
    {
        '_id': 'p_bolts_nuts',
        'name': 'Bolts and Nuts',
        'slug': 'bolts-nuts',
        'sku': 'IND-BLT-NUTS',
        'description': 'Grade 8.8 high-tensile carbon steel hex bolts and matching hex nuts. Hot-dip galvanized for extreme outdoor rust resistance.',
        'short_description': 'Grade 8.8 galvanized hex head structural bolts and nuts.',
        'features': ['High tensile steel (Grade 8.8)', 'Hot-dip galvanized coating', 'Full threads for secure fastening'],
        'specifications': [{'key': 'Material', 'value': 'Carbon Steel'}],
        'images': [{'url': '/static/images/products/plumbing/bolts_and_nuts.webp', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipe-fittings',
        'subcategory_slug': 'bolts-nuts',
        'brand_slug': 'standard',
        'brand_name': 'Standard',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_pipeline_clamps',
        'name': 'Pipeline Clamps',
        'slug': 'pipeline-clamps',
        'sku': 'IND-CLP-ALL',
        'description': 'Wide range of industrial pipeline installation clamps, including GI U-Bolt clamps, Cushioned special clamps, Motor L-angle supports, Bore dummies, and Bore clamps.',
        'short_description': 'Complete range of pipeline support clamps and covers.',
        'features': ['Vibration-dampening cushioning', 'High-strength steel fabrication', 'Corrosion-proof galvanizing'],
        'specifications': [{'key': 'Clamps Included', 'value': 'GI U Clamps, Special Clamps, Motor L angle clamps, Bore dummies, Bore Clamps'}],
        'images': [{'url': '/static/images/products/plumbing/pipeline_clamps.jpg', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipe-fittings',
        'subcategory_slug': 'pipeline-clamps',
        'brand_slug': 'standard',
        'brand_name': 'Standard',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_pump_sub',
        'name': 'CRI Submersible Pump',
        'slug': 'cri-submersible-pump',
        'sku': 'CRI-PMP-SUB',
        'description': 'Premium multi-stage CRI submersible borewell water pump. Corrosion-resistant stainless steel body, energy-efficient motor winding.',
        'short_description': 'CRI high-performance stainless steel submersible pump.',
        'features': ['Stainless Steel Grade 304 body', 'Energy efficient copper winding motor', 'High water discharge head capacity'],
        'specifications': [{'key': 'Brand', 'value': 'CRI'}, {'key': 'Phase', 'value': 'Single Phase / Three Phase'}],
        'images': [{'url': '/static/images/products/plumbing/cri_submersible_pumps.png', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pumps',
        'subcategory_slug': 'submersible-pumps',
        'brand_slug': 'cri',
        'brand_name': 'CRI',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_power_tools',
        'name': 'Power Tools',
        'slug': 'power-tools',
        'sku': 'IND-PWT-ALL',
        'description': 'Industrial grade corded and cordless power tools from leading global manufacturers. Select your preferred brand variant below.',
        'short_description': 'Heavy duty industrial power tools from global brands.',
        'features': ['Brushless motor technology', 'High impact drilling power', 'Long jobsite durability'],
        'specifications': [{'key': 'Product Type', 'value': 'Power Tools'}],
        'images': [{'url': '/static/images/products/plumbing/power_tools.avif', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pumps',
        'subcategory_slug': 'power-tools',
        'brand_slug': 'multiple',
        'brand_name': 'Bosch / DeWalt / Polymach / Valley Wolf',
        'available_brands': [
            {
                'brand_name': 'Bosch',
                'name': 'Bosch Professional Cordless Power Tools',
                'sku': 'IND-PWT-BOSCH',
                'image': '/static/images/products/plumbing/bosch-power-tools.jpg'
            },
            {
                'brand_name': 'DeWalt',
                'name': 'DeWalt Heavy Duty Power Tools',
                'sku': 'IND-PWT-DEWALT',
                'image': '/static/images/products/plumbing/dewalt_power_tools.jpeg'
            },
            {
                'brand_name': 'Polymach',
                'name': 'Polymak powertools',
                'sku': 'IND-PWT-POLY',
                'image': '/static/images/products/plumbing/polymak_powertools.jpg'
            },
            {
                'brand_name': 'Valley Wolf',
                'name': 'Ralli wolf power tools',
                'sku': 'IND-PWT-VWOLF',
                'image': '/static/images/products/plumbing/ralli_wolf_power_tools.jpg'
            }
        ],
        'available_brand_slugs': ['bosch', 'dewalt', 'polymach', 'valley-wolf'],
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_etool_taparia',
        'name': 'Taparia Engineering Tools',
        'slug': 'taparia-engineering-tools',
        'sku': 'IND-ENG-TAPARIA',
        'description': 'Taparia brand professional grade engineering hand tools, including double ended spanners, pipe wrenches, adjustable pliers, and socket sets.',
        'short_description': 'Professional grade spanners, wrenches, and hand tools from Taparia.',
        'features': ['Drop forged chrome vanadium steel', 'Rust preventive black phosphate finish', 'Meets IS/DIN industrial quality standards'],
        'specifications': [{'key': 'Brand', 'value': 'Taparia'}, {'key': 'Material', 'value': 'Chrome Vanadium Steel'}],
        'images': [{'url': '/static/images/products/plumbing/taparia_engineering_tools.jpeg', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pumps',
        'subcategory_slug': 'engineering-tools',
        'brand_slug': 'taparia',
        'brand_name': 'Taparia',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_tap_spindle',
        'name': 'Tap Spindle',
        'slug': 'tap-spindle',
        'sku': 'IND-FIT-SPINDLE',
        'description': 'Precision machined heavy brass replacement tap spindles with high-grade rubber washers and ceramic half-turn discs to stop leakages.',
        'short_description': 'Replacement brass tap spindles for standard plumbing taps.',
        'features': ['Solid extruded brass construction', 'Ceramic disc leak-proof seal', 'Universal standard thread sizing'],
        'specifications': [{'key': 'Material', 'value': 'Brass'}],
        'images': [{'url': '/static/images/products/plumbing/tap_spindle.jpeg', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipe-fittings',
        'subcategory_slug': 'tap-spindles',
        'brand_slug': 'standard',
        'brand_name': 'Standard',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_switches',
        'name': 'Switches',
        'slug': 'switches',
        'sku': 'IND-ELC-SWITCH',
        'description': 'Premium modular electrical switches for home and industrial use. Select your preferred brand variant below.',
        'short_description': 'Premium modular switches from Roma and Oswin.',
        'features': ['Modular design', 'Fire-retardant polycarbonate material', 'Smooth quiet operation'],
        'specifications': [{'key': 'Product Type', 'value': 'Modular Switches'}],
        'images': [{'url': '/static/images/products/plumbing/switches.png', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipe-fittings',
        'subcategory_slug': 'electrical-switches',
        'brand_slug': 'multiple',
        'brand_name': 'Roma / Oswin',
        'available_brands': [
            {
                'brand_name': 'Roma',
                'name': 'Anchor Roma Switches',
                'sku': 'IND-ELC-SWITCH-ROMA',
                'image': '/static/images/products/plumbing/anchor_roma_switches.jpeg'
            },
            {
                'brand_name': 'Oswin',
                'name': 'Switches',
                'sku': 'IND-ELC-SWITCH-OSWIN',
                'image': '/static/images/products/plumbing/switches.png'
            }
        ],
        'available_brand_slugs': ['roma', 'oswin'],
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_mcb_legrand',
        'name': 'Legrand MCB',
        'slug': 'legrand-mcb',
        'sku': 'IND-ELC-LEGRANDMCB',
        'description': 'Legrand brand Miniature Circuit Breakers (MCB) for overload and short-circuit protection in residential and commercial installations.',
        'short_description': 'Miniature Circuit Breakers (MCB) from Legrand.',
        'features': ['High breaking capacity', 'Touch-proof terminals', 'Bi-stable DIN rail clip'],
        'specifications': [{'key': 'Brand', 'value': 'Legrand'}, {'key': 'Current Rating', 'value': '6A - 63A'}],
        'images': [{'url': '/static/images/products/plumbing/legrand_mcb.jpg', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipe-fittings',
        'subcategory_slug': 'electrical-mcb',
        'brand_slug': 'legrand',
        'brand_name': 'Legrand',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'p_wires',
        'name': 'Wires',
        'slug': 'wires',
        'sku': 'IND-ELC-WIRE',
        'description': 'Multi-strand flexible copper wires for electrical conduit installation. High conductivity, 100% flame retardant PVC insulation.',
        'short_description': 'Flame retardant electrical wires from Finolex and Orbit.',
        'features': ['100% Electrolytic copper conductor', 'Flame Retardant (FR) PVC insulation', 'RoHS and ISI certified'],
        'specifications': [{'key': 'Product Type', 'value': 'Electrical Wires'}],
        'images': [{'url': '/static/images/products/plumbing/wires_common.jpg', 'is_primary': True}],
        'business_slug': 'plumbing',
        'category_slug': 'pipes',
        'subcategory_slug': 'electrical-wires',
        'brand_slug': 'multiple',
        'brand_name': 'Finolex / Orbit',
        'available_brands': [
            {
                'brand_name': 'Finolex',
                'name': 'Finolex Electrical Wires',
                'sku': 'IND-ELC-WIRE-FINOLEX',
                'image': '/static/images/products/plumbing/wires_common.jpg'
            },
            {
                'brand_name': 'Orbit',
                'name': 'Orbit Electrical Wires',
                'sku': 'IND-ELC-WIRE-ORBIT',
                'image': '/static/images/products/plumbing/wires_common.jpg'
            }
        ],
        'available_brand_slugs': ['finolex', 'orbit'],
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },

    # --- HARDWARE STORE PRODUCTS ---
    {
        '_id': 'h_paints',
        'name': 'Paints',
        'slug': 'paints',
        'sku': 'HDW-PNT-ALL',
        'description': 'Premium high-durability paints for interior walls, exterior facades, metal, and wood finishing. Choose from top brands below.',
        'short_description': 'Premium paints from Asian Paints, MRF, and Sheenlac.',
        'features': ['High coverage area', 'Washable wall finish', 'Anti-fungal and weather resistant'],
        'specifications': [{'key': 'Product Type', 'value': 'Premium Paints'}],
        'images': [{'url': '/static/images/products/hardware/paints_common.jpg', 'is_primary': True}],
        'business_slug': 'hardware',
        'category_slug': 'paints-chemicals',
        'subcategory_slug': 'paints',
        'brand_slug': 'multiple',
        'brand_name': 'Asian Paints / MRF / Sheenlac',
        'available_brands': [
            {
                'brand_name': 'Asian Paints',
                'name': 'Asian Paints Premium Wall Emulsion',
                'sku': 'HDW-PNT-ASIAN',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'MRF paints',
                'name': 'MRF Wood & Metal Paints',
                'sku': 'HDW-PNT-MRF',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'Sheenlac Paints',
                'name': 'Sheenlac Wood Polish & Paints',
                'sku': 'HDW-PNT-SHEENLAC',
                'image': '/static/images/placeholder.jpg'
            }
        ],
        'available_brand_slugs': ['asian-paints', 'mrf-paints', 'sheenlac-paints'],
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'h_white_cement',
        'name': 'White Cement',
        'slug': 'white-cement',
        'sku': 'HDW-WCM-ALL',
        'description': 'Ultra-white cement for wall putty preparation, tile grouting, and decorative concrete works. Excellent bonding strength.',
        'short_description': 'High-grade white cement from Birla and JK.',
        'features': ['High refractive index for whiteness', 'Smooth plaster finish', 'Durable compressive strength'],
        'specifications': [{'key': 'Product Type', 'value': 'White Cement'}],
        'images': [{'url': '/static/images/products/hardware/white_cement_common.jpg', 'is_primary': True}],
        'business_slug': 'hardware',
        'category_slug': 'paints-chemicals',
        'subcategory_slug': 'white-cement',
        'brand_slug': 'multiple',
        'brand_name': 'Birla / JK',
        'available_brands': [
            {
                'brand_name': 'Birla',
                'name': 'Birla White Cement',
                'sku': 'HDW-WCM-BIRLA',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'JK',
                'name': 'JK White Cement',
                'sku': 'HDW-WCM-JK',
                'image': '/static/images/placeholder.jpg'
            }
        ],
        'available_brand_slugs': ['birla', 'jk'],
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'h_waterproofing',
        'name': 'Water Proofing Chemicals',
        'slug': 'waterproofing-chemicals',
        'sku': 'HDW-WPF-ALL',
        'description': 'Advanced waterproofing chemicals, acrylic coatings, and elastomeric water-barrier additives for terraces, basements, and wet areas.',
        'short_description': 'Waterproofing chemical additives from Dr.Fixit, Fosroc, and Sika.',
        'features': ['Excellent water resistance', 'High elasticity & crack bridging', 'Durable protective layer'],
        'specifications': [{'key': 'Product Type', 'value': 'Waterproofing Chemicals'}],
        'images': [{'url': '/static/images/products/hardware/waterproofing_common.jpg', 'is_primary': True}],
        'business_slug': 'hardware',
        'category_slug': 'paints-chemicals',
        'subcategory_slug': 'waterproofing-chemicals',
        'brand_slug': 'multiple',
        'brand_name': 'Dr.Fixit / Fosroc / Sika',
        'available_brands': [
            {
                'brand_name': 'Dr.Fixit',
                'name': 'Dr.Fixit Waterproofing Chemical',
                'sku': 'HDW-WPF-DRFIXIT',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'Fosroc',
                'name': 'Fosroc Waterproofing Slurry',
                'sku': 'HDW-WPF-FOSROC',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'Sika',
                'name': 'Sika Waterproofing Mortar',
                'sku': 'HDW-WPF-SIKA',
                'image': '/static/images/placeholder.jpg'
            }
        ],
        'available_brand_slugs': ['dr-fixit', 'fosroc', 'sika'],
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'h_adhesives',
        'name': 'Adhesive',
        'slug': 'adhesives',
        'sku': 'HDW-ADH-ALL',
        'description': 'Heavy-duty structural adhesives, synthetic wood glues, high-strength tile adhesives, and epoxy resins for diverse construction applications.',
        'short_description': 'Premium adhesives from Fevicol, Raaf, CeraBond, MYK, Araldite, and Bondite.',
        'features': ['Exceptional bonding strength', 'Fast curing formulas', 'Moisture and thermal resistance'],
        'specifications': [{'key': 'Product Type', 'value': 'Industrial Adhesives'}],
        'images': [{'url': '/static/images/products/hardware/adhesives_common.jpg', 'is_primary': True}],
        'business_slug': 'hardware',
        'category_slug': 'paints-chemicals',
        'subcategory_slug': 'adhesives',
        'brand_slug': 'multiple',
        'brand_name': 'Fevicol / Raaf / CeraBond / MYK / Araldite / Bondite',
        'available_brands': [
            {
                'brand_name': 'fevicol',
                'name': 'Fevicol SH Synthetic Adhesive',
                'sku': 'HDW-ADH-FEVICOL',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'Raaf',
                'name': 'Raaf Premium Wood Adhesive',
                'sku': 'HDW-ADH-RAAF',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'CeraBond',
                'name': 'CeraBond Tile Adhesive',
                'sku': 'HDW-ADH-CERABOND',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'MYK',
                'name': 'MYK Laticrete Tile Adhesive',
                'sku': 'HDW-ADH-MYK',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'Araldite',
                'name': 'Araldite Standard Epoxy Adhesive',
                'sku': 'HDW-ADH-ARALDITE',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'Bondite',
                'name': 'Bondite General Purpose Adhesive',
                'sku': 'HDW-ADH-BONDITE',
                'image': '/static/images/placeholder.jpg'
            }
        ],
        'available_brand_slugs': ['fevicol', 'raaf', 'cerabond', 'myk', 'araldite', 'bondite'],
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'h_locks',
        'name': 'Locks',
        'slug': 'locks',
        'sku': 'HDW-LCK-ALL',
        'description': 'High-security mechanical and digital mortise locks, night latches, padlocks, and smart main-door locks.',
        'short_description': 'Premium security locks from Godrej, Europa, and Yale.',
        'features': ['Drill and pick resistant keys', 'Heavy-duty steel bolt locks', 'Smooth latch operations'],
        'specifications': [{'key': 'Product Type', 'value': 'Security Door Locks'}],
        'images': [{'url': '/static/images/products/hardware/locks_common.jpg', 'is_primary': True}],
        'business_slug': 'hardware',
        'category_slug': 'door-hardware',
        'subcategory_slug': 'locks',
        'brand_slug': 'multiple',
        'brand_name': 'Godrej / Europa / Yale',
        'available_brands': [
            {
                'brand_name': 'Godrej',
                'name': 'Godrej Classic Mortise Lock',
                'sku': 'HDW-LCK-GODREJ',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'Europa',
                'name': 'Europa Double Action Night Latch',
                'sku': 'HDW-LCK-EUROPA',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'Yale',
                'name': 'Yale Digital Smart Door Lock',
                'sku': 'HDW-LCK-YALE',
                'image': '/static/images/placeholder.jpg'
            }
        ],
        'available_brand_slugs': ['godrej', 'europa', 'yale'],
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'h_hinges',
        'name': 'Hinges',
        'slug': 'hinges',
        'sku': 'HDW-HNG-SS',
        'description': 'Heavy-duty stainless steel ball-bearing door hinges, cabinet hinges, and hydraulic soft-close fittings.',
        'short_description': 'Stainless steel door hinges and fittings.',
        'features': ['Corrosion-resistant stainless steel', 'Ball-bearing smooth rotation', 'High load capacity'],
        'specifications': [{'key': 'Material', 'value': 'Stainless Steel'}],
        'images': [{'url': '/static/images/products/hardware/hinges_common.jpg', 'is_primary': True}],
        'business_slug': 'hardware',
        'category_slug': 'door-hardware',
        'subcategory_slug': 'hinges',
        'brand_slug': 'standard',
        'brand_name': 'Standard',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': False,
        'is_new': False
    },
    {
        '_id': 'h_tower_bolts',
        'name': 'Tower Bolts',
        'slug': 'tower-bolts',
        'sku': 'HDW-TBL-BR',
        'description': 'Solid brass and stainless steel tower bolts for sliding security lock reinforcement on main and bathroom doors.',
        'short_description': 'Brass and steel security tower bolts.',
        'features': ['Heavy solid bolt rod', 'Smooth slide lock mechanism', 'Tamper proof mounting'],
        'specifications': [{'key': 'Material', 'value': 'Solid Brass / Steel'}],
        'images': [{'url': '/static/images/products/hardware/tower_bolts_common.jpg', 'is_primary': True}],
        'business_slug': 'hardware',
        'category_slug': 'door-hardware',
        'subcategory_slug': 'tower-bolts',
        'brand_slug': 'standard',
        'brand_name': 'Standard',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': False,
        'is_new': False
    },
    {
        '_id': 'h_altraps',
        'name': 'Altraps',
        'slug': 'altraps',
        'sku': 'HDW-ALT-HD',
        'description': 'Heavy-duty steel altraps and padlock latch fittings designed for outer security gates and shop doors.',
        'short_description': 'Security gate altraps and padlock latches.',
        'features': ['Reinforced steel construction', 'Weatherproof plating', 'Fits standard padlocks'],
        'specifications': [{'key': 'Material', 'value': 'Reinforced Steel'}],
        'images': [{'url': '/static/images/products/hardware/altraps_common.jpg', 'is_primary': True}],
        'business_slug': 'hardware',
        'category_slug': 'door-hardware',
        'subcategory_slug': 'altraps',
        'brand_slug': 'standard',
        'brand_name': 'Standard',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': False,
        'is_new': False
    },
    {
        '_id': 'h_tile_beeding_paser',
        'name': 'Tile Beeding and Paser',
        'slug': 'tile-beeding-and-paser',
        'sku': 'HDW-TBP-GEN',
        'description': 'Plastic tile alignment spacers (paser) and protective round-edge tile border beading profiles for clean joint masonry.',
        'short_description': 'Tile border beeding and joint spacing markers.',
        'features': ['Precision joint spacing (2mm, 3mm, 4mm)', 'PVC and metal edge beading profiles', 'Ensures clean grout alignment'],
        'specifications': [{'key': 'Application', 'value': 'Ceramic & Vitrified Tiles Installation'}],
        'images': [{'url': '/static/images/products/hardware/tile_beeding_common.jpg', 'is_primary': True}],
        'business_slug': 'hardware',
        'category_slug': 'door-hardware',
        'subcategory_slug': 'tile-beeding-paser',
        'brand_slug': 'standard',
        'brand_name': 'Standard',
        'hide_brand_badge': True,
        'is_active': True,
        'is_featured': False,
        'is_new': False
    },
    {
        '_id': 'h_fans',
        'name': 'Fans',
        'slug': 'fans',
        'sku': 'HDW-FAN-ALL',
        'description': 'High-performance ceiling fans, decorative fans, wall fans, and silent kitchen/bathroom exhaust fans from top brands.',
        'short_description': 'Energy-efficient home fans from Crompton, Havells, Kayton, and GM.',
        'features': ['High air delivery motor', '5-Star energy efficiency rating', 'Corrosion-proof paint coat'],
        'specifications': [{'key': 'Product Type', 'value': 'Electric Fans'}],
        'images': [{'url': '/static/images/products/hardware/fans_common.jpg', 'is_primary': True}],
        'business_slug': 'hardware',
        'category_slug': 'electrical-fans',
        'subcategory_slug': 'fans',
        'brand_slug': 'multiple',
        'brand_name': 'Crompton / Havells / Kayton / GM',
        'available_brands': [
            {
                'brand_name': 'Crompton',
                'name': 'Crompton High Speed Ceiling Fan',
                'sku': 'HDW-FAN-CROMPTON',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'Havells',
                'name': 'Havells Decorative Ceiling Fan',
                'sku': 'HDW-FAN-HAVELLS',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'Kayton',
                'name': 'Kayton Classic Fan',
                'sku': 'HDW-FAN-KAYTON',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'GM',
                'name': 'GM Modular Exhaust Fan',
                'sku': 'HDW-FAN-GM',
                'image': '/static/images/placeholder.jpg'
            }
        ],
        'available_brand_slugs': ['crompton', 'havells', 'kayton', 'gm'],
        'is_active': True,
        'is_featured': True,
        'is_new': True
    },
    {
        '_id': 'h_led_lights',
        'name': 'LED lights',
        'slug': 'led-lights',
        'sku': 'HDW-LED-ALL',
        'description': 'Energy-saving home lighting solutions, including LED bulbs, slim panel lights, spotlights, and wall batten lights.',
        'short_description': 'Premium LED lights from Philips, GM, Looker, and Surya.',
        'features': ['Long life (up to 25,000 hours)', 'High lumens per watt output', 'Surge protection integrated'],
        'specifications': [{'key': 'Product Type', 'value': 'LED Lighting'}],
        'images': [{'url': '/static/images/products/hardware/led_lights_common.jpg', 'is_primary': True}],
        'business_slug': 'hardware',
        'category_slug': 'electrical-fans',
        'subcategory_slug': 'led-lights',
        'brand_slug': 'multiple',
        'brand_name': 'Philips / GM / Looker / Surya',
        'available_brands': [
            {
                'brand_name': 'Philips',
                'name': 'Philips Bright LED Bulbs',
                'sku': 'HDW-LED-PHILIPS',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'GM',
                'name': 'GM Modular LED Panel Light',
                'sku': 'HDW-LED-GM',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'Looker',
                'name': 'Looker COB Downlight',
                'sku': 'HDW-LED-LOOKER',
                'image': '/static/images/placeholder.jpg'
            },
            {
                'brand_name': 'Surya',
                'name': 'Surya Slim Fit LED Batten',
                'sku': 'HDW-LED-SURYA',
                'image': '/static/images/placeholder.jpg'
            }
        ],
        'available_brand_slugs': ['philips', 'gm', 'looker', 'surya'],
        'is_active': True,
        'is_featured': True,
        'is_new': True
    }
]


