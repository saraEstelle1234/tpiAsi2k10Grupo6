with open('scripts_y_notas/generate_v8_deck.py', 'r', encoding='utf-8') as f:
    deck = f.read()

# Let's find where </style> is
style_idx = deck.find('</style>')
if style_idx == -1:
    print("Error: </style> not found")
else:
    print(f"</style> found at index {style_idx}")
    print("Preceding 200 chars:")
    print(deck[style_idx-200:style_idx])
