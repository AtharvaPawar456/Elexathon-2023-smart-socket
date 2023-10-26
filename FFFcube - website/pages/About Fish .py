import streamlit as st

allDetails = [                '''
                Goldfish are a popular freshwater fish that are often kept as pets in aquariums. Here are some details about Goldfish:

                Scientific name: Carassius auratus
                Origin: China
                Size: Goldfish can grow up to 12 inches (30 cm) in length, depending on the species and living conditions.
                Lifespan: With proper care, Goldfish can live for 10 to 20 years or even longer.
                Appearance: Goldfish are typically orange or gold in color, but can also be white, black, or a combination of colors. They have a round, flattened body shape and are known for their distinctive fan-shaped tail and double tail.
                Diet: Goldfish are omnivores and can eat a variety of foods, including fish flakes, pellets, and live or frozen foods such as brine shrimp and bloodworms.
                Water parameters: Goldfish are coldwater fish and prefer water temperatures between 65-72°F (18-22°C). They also require a well-oxygenated and filtered aquarium with a pH range of 6.0 to 8.0 and moderate water hardness.
                Behavior: Goldfish are social animals and prefer to be kept in groups. They are active swimmers and enjoy having plenty of swimming space and places to hide and explore in their aquarium.
                Care requirements: Goldfish require regular maintenance and care, including monitoring water quality, performing partial water changes, and cleaning the aquarium. They also need a suitable-sized aquarium with adequate filtration and aeration, and should not be kept in bowls or small tanks.
                ''',
                '''
                Angelfish are a popular freshwater fish that are known for their distinctive appearance and graceful swimming behavior. Here are some details about Angelfish:

                Scientific name: Pterophyllum scalare
                Origin: South America, specifically the Amazon River basin
                Size: Angelfish can grow up to 6 inches (15 cm) in length, depending on the species and living conditions.
                Lifespan: With proper care, Angelfish can live for 8 to 10 years or even longer.
                Appearance: Angelfish have a triangular body shape with elongated fins that give them a graceful appearance. They are typically silver or silver-grey in color, with black vertical stripes that extend from their dorsal fin to their anal fin. There are also several color variants of Angelfish available in the aquarium trade, including albino, gold, and black.
                Diet: Angelfish are omnivores and can eat a variety of foods, including fish flakes, pellets, and live or frozen foods such as brine shrimp and bloodworms.
                Water parameters: Angelfish are tropical fish and require water temperatures between 75-82°F (24-28°C). They also require a well-oxygenated and filtered aquarium with a pH range of 6.5 to 7.5 and moderate water hardness.
                Behavior: Angelfish are peaceful fish that can be kept in groups or pairs. They are active swimmers and enjoy having plenty of swimming space and places to hide and explore in their aquarium.
                Care requirements: Angelfish require regular maintenance and care, including monitoring water quality, performing partial water changes, and cleaning the aquarium. They also need a suitable-sized aquarium with adequate filtration and aeration, and should not be kept in bowls or small tanks.
                ''',
                '''
                Guppies are small and colorful freshwater fish that are very popular in the aquarium trade. Here are some details about guppies:

                Scientific name: Poecilia reticulata
                Origin: Native to Northeast South America, specifically Guyana, Trinidad, and Brazil.
                Size: Guppies are small fish and typically grow to be around 1-2 inches (2.5-5 cm) in length.
                Lifespan: Guppies have a relatively short lifespan and usually live for around 2-3 years.
                Appearance: Male guppies are more colorful than females and have striking patterns of bright blue, orange, and green on their bodies and fins. Females are typically less colorful and have a more subdued appearance. There are also several different color variations of guppies available in the aquarium trade, including leopard, tuxedo, and neon.
                Diet: Guppies are omnivores and will eat a variety of foods, including flakes, pellets, and live or frozen foods such as brine shrimp and bloodworms.
                Water parameters: Guppies are tropical fish and require water temperatures between 75-82°F (24-28°C). They also require a well-oxygenated and filtered aquarium with a pH range of 7.0 to 8.0 and moderate water hardness.
                Behavior: Guppies are peaceful fish that can be kept in groups or pairs. They are active swimmers and enjoy having plenty of swimming space and places to hide and explore in their aquarium.
                Care requirements: Guppies require regular maintenance and care, including monitoring water quality, performing partial water changes, and cleaning the aquarium. They also need a suitable-sized aquarium with adequate filtration and aeration, and should not be kept in bowls or small tanks.
                ''',
                '''
                Catfish are a diverse group of freshwater fish that are found all over the world. Here are some details about catfish:

                Scientific name: There are many species of catfish, belonging to several different families, including the Ictaluridae, Pimelodidae, and Siluridae families.
                Origin: Catfish can be found in freshwater habitats all over the world, including rivers, lakes, and streams.
                Size: The size of catfish can vary greatly depending on the species, but many catfish can grow to be quite large. The largest catfish species, the Mekong giant catfish, can grow up to 10 feet (3 meters) in length and weigh up to 660 pounds (300 kilograms).
                Appearance: Catfish come in a wide variety of shapes and colors. Many species have a distinctive "whisker-like" barbels around their mouth, which they use to sense their environment and locate food. Some catfish species have a smooth, scaleless skin, while others have an armored, bony plates covering their bodies.
                Diet: Catfish are opportunistic feeders and will eat a wide variety of food, including insects, small fish, crustaceans, and plant matter.
                Water parameters: The water parameters required for catfish can vary depending on the species. In general, they prefer warm water temperatures between 75-82°F (24-28°C) and a pH range between 6.5-7.5.
                Behavior: Catfish are typically nocturnal and spend much of their time hiding during the day. They are generally peaceful fish, but some species can become territorial or aggressive towards other fish.
                Care requirements: Catfish require a suitable-sized aquarium with plenty of hiding places and appropriate water quality. Some species may also require a specific diet or water parameters. It's important to research the specific needs of the species of catfish you are interested in keeping before adding them to your aquarium.
                ''',
                '''
                Tetras are a group of small, brightly-colored freshwater fish that are popular in the aquarium hobby. Here are some details about tetras:

                Scientific name: There are many species of tetras, belonging to the Characidae family.
                Origin: Tetras are native to South America, but many species have been introduced to other parts of the world and are now found in other regions, such as Southeast Asia.
                Size: Tetras are generally small fish, typically growing to around 1-2 inches (2.5-5 cm) in length.
                Appearance: Tetras are known for their bright, vivid colors, which can include red, blue, green, and yellow. Many species also have iridescent scales that can reflect light in a variety of colors. Some common tetra species include the neon tetra, cardinal tetra, and black skirt tetra.
                Diet: Tetras are omnivores and will eat a variety of food, including small insects, crustaceans, and plant matter. In the aquarium, they can be fed a diet of flakes, pellets, and frozen foods.
                Water parameters: Tetras prefer slightly acidic water with a pH range between 6.0-7.0 and a water temperature between 72-82°F (22-28°C).
                Behavior: Tetras are generally peaceful and social fish that do well in groups. They are active swimmers and should be provided with plenty of open swimming space in the aquarium.
                Care requirements: Tetras require a suitable-sized aquarium with plenty of hiding places and appropriate water quality. They can be sensitive to changes in water parameters, so it's important to maintain stable conditions in the aquarium. It's also important to keep them with compatible tankmates, as some species may be nippy or aggressive towards other fish.
                ''',
                '''
                Molly is a popular freshwater fish species that belongs to the Poecilia genus of the Poeciliidae family. Here are some details about molly:

                Origin: Molly is native to Central and South America, but they are now found in many parts of the world, including Asia and Africa, due to their popularity in the aquarium trade.
                Size: Mollies are relatively small, usually growing to about 3-4 inches (7-10 cm) in length.
                Appearance: Mollies come in a variety of colors, including black, silver, orange, and yellow. Some have a speckled or spotted pattern, and others may have a solid color. They have a sleek, streamlined body with a pointed head and a rounded tail.
                Diet: Mollies are omnivorous and will eat a variety of foods, including algae, small insects, and crustaceans. In the aquarium, they can be fed a diet of flakes, pellets, and frozen foods.
                Water parameters: Mollies prefer slightly alkaline water with a pH range between 7.5-8.5 and a water temperature between 75-82°F (24-28°C). They also prefer hard water with a high mineral content.
                Behavior: Mollies are generally peaceful fish that do well in groups. They are active swimmers and should be provided with plenty of open swimming space in the aquarium. Males can sometimes be aggressive towards each other, so it's important to keep a higher number of females in the group.
                Care requirements: Mollies require a suitable-sized aquarium with plenty of hiding places and appropriate water quality. They can be sensitive to changes in water parameters, so it's important to maintain stable conditions in the aquarium. They also prefer a planted aquarium with plenty of vegetation to hide in.
                ''',
                '''
                Knife fish is a type of freshwater fish that belongs to the Gymnotiformes order. Here are some details about knife fish:

                Origin: Knife fish are native to the rivers and streams of South America, particularly the Amazon basin.
                Size: Knife fish can vary in size depending on the species, but they typically grow to be between 6 and 24 inches (15-60 cm) in length.
                Appearance: Knife fish have a long, narrow body that is flattened from side to side, resembling a knife blade. They are typically brown or gray in color and have a distinctive dorsal fin that runs the length of their body. They have a small mouth and no scales.
                Diet: Knife fish are carnivorous and primarily feed on other fish, insects, and crustaceans.
                Water parameters: Knife fish prefer slightly acidic to neutral water with a pH range between 6.0-7.5 and a water temperature between 75-82°F (24-28°C). They also prefer soft water with a low mineral content.
                Behavior: Knife fish are nocturnal and tend to be active at night. They have a weak electric field around their body that they use to navigate and locate prey. Knife fish are generally peaceful, but they can be territorial and aggressive towards their own species.
                Care requirements: Knife fish require a large aquarium with plenty of hiding places and open swimming space. They prefer a dimly lit aquarium and will appreciate the presence of live plants. Because they are carnivorous, they can produce a lot of waste, so a strong filtration system is important to maintain good water quality. It's also important to provide them with appropriate tank mates, as they can be aggressive towards other fish.
                ''',
                '''
                Plecostomus, also known as plecos, are a type of freshwater catfish that belong to the Loricariidae family. Here are some details about plecostomus:

                Origin: Plecos are native to South America, particularly the Amazon basin.
                Size: Plecos can vary in size depending on the species, but they typically grow to be between 6 and 24 inches (15-60 cm) in length.
                Appearance: Plecos have a flat, wide body that is covered in bony plates. They have a distinctive sucker mouth that they use to attach to surfaces and scrape algae and other food sources. Plecos can vary in color and pattern, with some species having spots or stripes.
                Diet: Plecos are omnivorous and primarily feed on algae, but they will also eat other plant matter and small invertebrates.
                Water parameters: Plecos prefer slightly acidic to neutral water with a pH range between 6.5-7.5 and a water temperature between 72-86°F (22-30°C). They also prefer soft to moderately hard water.
                Behavior: Plecos are generally peaceful and can be kept with a variety of tank mates. They are nocturnal and will spend much of their time hiding during the day. Plecos can be territorial towards their own species and may fight over hiding places or food.
                Care requirements: Plecos require a large aquarium with plenty of hiding places and open swimming space. They appreciate the presence of live plants and driftwood, which they will use for hiding and grazing. Because they are omnivorous, they can produce a lot of waste, so a strong filtration system is important to maintain good water quality. It's also important to provide them with appropriate tank mates and plenty of food sources to prevent them from becoming aggressive or territorial.
                ''',
                '''
                There are many species of sharks, so the details can vary depending on which specific species you are referring to. However, here are some general details about sharks:

                Origin: Sharks are found in oceans all over the world, from warm tropical waters to cold polar regions.
                Size: The size of a shark can vary greatly depending on the species. Some, like the dwarf lantern shark, grow to be only a few inches long, while others, like the whale shark, can reach lengths of over 40 feet (12 meters).
                Appearance: Sharks are characterized by their cartilaginous skeleton, five to seven gill slits on the sides of their heads, and a series of sharp teeth. They have a streamlined body shape that helps them move quickly through the water.
                Diet: Sharks are carnivores and eat a variety of prey, including fish, squid, octopus, and marine mammals. Some species, like the whale shark, are filter feeders and eat plankton.
                Water parameters: Sharks are adapted to living in saltwater environments and require specific water parameters depending on the species. They can be found in both shallow and deep waters.
                Behavior: Sharks are generally solitary animals and may be territorial. Some species, like the great white shark, are known to be aggressive towards humans, while others, like the nurse shark, are relatively docile.
                Care requirements: Due to their large size and predatory nature, sharks are not suitable for most home aquariums. They require very large tanks with specialized filtration systems and a carefully selected diet. Sharks are also often protected by law, so it is important to check with your local regulations before attempting to keep one as a pet.
                ''',
                '''
                Gouramis are a group of freshwater fish that belong to the family Osphronemidae. There are many different species of gouramis, but here are some general details:

                Origin: Gouramis are native to Southeast Asia, where they are found in a variety of freshwater habitats, including rivers, lakes, and swamps.
                Size: The size of a gourami can vary depending on the species, but most grow to be between 2 and 6 inches (5 to 15 cm) in length.
                Appearance: Gouramis have a distinctive elongated body shape and a pointed head. They come in a variety of colors, including blue, red, green, and gold. Some species, like the dwarf gourami, have a pattern of spots or stripes on their body.
                Diet: Gouramis are omnivores and will eat a variety of foods, including small invertebrates, algae, and plant matter. In captivity, they can be fed a combination of commercial fish food and live or frozen foods.
                Water parameters: Gouramis prefer warm, still or slow-moving water with a slightly acidic to neutral pH (around 6.0 to 7.5). They are also sensitive to changes in water quality and require regular water changes to maintain good health.
                Behavior: Gouramis are generally peaceful fish and can be kept with other peaceful community fish. However, males of some species can be aggressive towards each other, so it is important to provide plenty of hiding places and territory for each fish.
                Care requirements: Gouramis are generally hardy fish and are easy to care for. They require a tank with plenty of hiding places and plants, as well as a gentle filtration system that does not create too much water movement.
                '''
                ]
def main():
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["Goldfish", "Angelfish", "Guppy", "Catfish", "Tetra", "Molly", "Knife", "Plecostomus", "Shark", "Gourami"])
    
    with tab1:
        colt1,colt2 = st.columns(2)
        with colt1:
            st.header("Goldfish")
            st.image("images\_fish-db\Goldfish.png", width=200)
        with colt2:
            st.markdown(allDetails[0])

    with tab2:
        colt1,colt2 = st.columns(2)
        with colt1:
            st.header("Angelfish")
            st.image("images\_fish-db\Angelfish.png", width=200)
        with colt2:
            st.markdown(allDetails[1])

    with tab3:
        colt1,colt2 = st.columns(2)
        with colt1:
            st.header("Guppy")
            st.image("images\_fish-db\Guppy.png", width=200)
        with colt2:
            st.markdown(allDetails[2])
        
    with tab4:
        colt1,colt2 = st.columns(2)
        with colt1:
            st.header("Catfish")
            st.image("images\_fish-db\Catfish.png", width=200)
        with colt2:
            st.markdown(allDetails[3])

    with tab5:
        colt1,colt2 = st.columns(2)
        with colt1:
            st.header("Tetra")
            st.image("images\_fish-db\Tetra.png", width=200)
        with colt2:
            st.markdown(allDetails[4])

    with tab6:
        colt1,colt2 = st.columns(2)
        with colt1:
            st.header("Molly")
            st.image("images\_fish-db\Molly.png", width=200)
        with colt2:
            st.markdown(allDetails[5])

    with tab7:
        colt1,colt2 = st.columns(2)
        with colt1:
            st.header("Knife")
            st.image("images\_fish-db\Knife.png", width=200)
        with colt2:
            st.markdown(allDetails[6])

    with tab8:
        colt1,colt2 = st.columns(2)
        with colt1:
            st.header("Plecostomus")
            st.image("images\_fish-db\Plecostomus.png", width=200)
        with colt2:
            st.markdown(allDetails[7])

    with tab9:
        colt1,colt2 = st.columns(2)
        with colt1:
            st.header("Shark")
            st.image("images\_fish-db\Shark.png", width=200)
        with colt2:
            st.markdown(allDetails[8])

    with tab10:
        colt1,colt2 = st.columns(2)
        with colt1:
            st.header("Gourami")
            st.image("images\_fish-db\Gourami.png", width=200) 
        with colt2:
            st.markdown(allDetails[9])

if __name__ == '__main__':
    st.set_page_config(page_title="Fcube",
                       page_icon=":fish:",
                       layout="wide")
    st.title("About Fish")
    main()