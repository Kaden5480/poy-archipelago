using System;
using System.Collections.Generic;

using PoYArchipelago.AP.Data;

namespace PoYArchipelago.AP {
    public class Items {
        private IDHandler handler { get; }
        private Dictionary<long, ItemData> items { get; } = new Dictionary<long, ItemData>();

        // Extra stuff game manager doesn't track
        public bool hasNorthernTicket;
        public bool hasFundamentalsBook;
        public bool hasEssentialsBook;

        // Shorthand for interacting with GameManager.control
        private GameManager manager {
            get => GameManager.control;
        }

        /**
         * <summary>
         * Creates the data store for all items.
         * </summary>
         */
        public Items(IDHandler handler) {
            this.handler = handler;
        }

        /**
         * <summary>
         * Creates data for a new item, storing
         * information about it.
         * </summary>
         * <param name="name">The name of this item</param>
         * <param name="unlockMethod">The method to execute when this item is unlocked</param>
         */
        public void CreateItem(
            string name,
            Action unlockMethod
        ) {
            ItemData data = new ItemData(
                handler.NewID(), name, unlockMethod
            );
            items.Add(data.id, data);
        }

        /**
         * <summary>
         * Gets data for an item by its ID.
         * </summary>
         * <param name="id">The ID of the item to get data for</param>
         * <returns>The data for this item, null if not found</returns>
         */
        public ItemData Get(long id) {
            if (items.TryGetValue(id, out ItemData data) == true) {
                return data;
            }
            return null;
        }

        /**
         * <summary>
         * Creates data for all items.
         * </summary>
         */
        private void CreateAll() {

#region Base Game

            // NOTE: No need to store item names anywhere
            // an ID for an unlock is sent over, and that's all that
            // should be needed

            // Artefacts
            CreateItem("Hat #1",                   () => manager.hasArtefact_Hat1 = true);
            CreateItem("Hat #2",                   () => manager.hasArtefact_Hat2 = true);
            CreateItem("Shoe",                     () => manager.hasArtefact_Shoe = true);
            CreateItem("Sleeping Bag",             () => manager.hasArtefact_Sleepingbag = true);
            CreateItem("Safety Helmet",            () => manager.hasArtefact_Helmet = true);
            CreateItem("Backpack",                 () => manager.hasArtefact_Backpack = true);
            CreateItem("Shovel",                   () => manager.hasArtefact_Shovel = true);

            // Progressively unlock the photograph
            CreateItem("Picture Fragment", () => {
                if (manager.hasArtefact_Photograph1 == false)      manager.hasArtefact_Photograph1 = true;
                else if (manager.hasArtefact_Photograph2 == false) manager.hasArtefact_Photograph2 = true;
                else if (manager.hasArtefact_Photograph3 == false) manager.hasArtefact_Photograph3 = true;
                else if (manager.hasArtefact_Photograph4 == false) manager.hasArtefact_Photograph4 = true;
                else {
                    // NOTE: This should be unreachable
                }
            });
            // There is only one picture frame
            CreateItem("Picture Frame",            () => manager.hasArtefact_PhotographFrame = true);

            // Statues
            CreateItem("Fundamental Statue",       () => manager.hasArtefact_Statue0 = true);
            CreateItem("Intermediate Statue",      () => manager.hasArtefact_Statue1 = true);
            CreateItem("Advanced Statue",          () => manager.hasArtefact_Statue2 = true);
            CreateItem("Expert Statue",            () => manager.hasArtefact_Statue3 = true);

            // Consumables
            CreateItem("Bird Seeds +1",            () => manager.extraBirdSeedUses++);
            CreateItem("Chalk +2",                 () => manager.extraChalkUses += 2);
            CreateItem("Coffee +2",                () => manager.extraCoffeeUses += 2);
            CreateItem("Coffee +5",                () => manager.extraCoffeeUses += 5);
            CreateItem("Ropes +1",                 () => manager.ropesCollected++);
            CreateItem("Ropes +2",                 () => manager.ropesCollected += 2);

            // Tools
            CreateItem("Artefact Map",             () => manager.artefactMap = true);
            CreateItem("Barometer",                () => manager.barometer = true);
            CreateItem("Chalk Bag",                () => manager.chalkBag = true);
            CreateItem("Coffee Unlock",            () => manager.coffee = true);
            CreateItem("Crampons (6 Point)",       () => manager.crampons = true);
            CreateItem("Crampons (10 Point)",      () => manager.cramponsUpgrade = true);
            CreateItem("Ice Axes",                 () => manager.iceAxes = true);
            CreateItem("Monocular",                () => manager.monocular = true);
            CreateItem("Phonograph",               () => manager.phonograph = true);
            CreateItem("Pipe",                     () => manager.smokingpipe = true);
            CreateItem("Pocketwatch",              () => manager.pocketwatch = true);
            CreateItem("Rope Unlock",              () => manager.rope = true);
            CreateItem("Double Length Rope",       () => manager.ropesUpgrade = true);

            // Infinite things
            CreateItem("Infinite Chalk",           () => manager.extraChalkUses += 999999999);
            CreateItem("Infinite Coffee",          () => manager.extraCoffeeUses += 999999999);

            // Medals for all peaks
            CreateItem("Fundamentals Medal",       () => manager.npc_oas_category1 = true);
            CreateItem("Intermediate Medal",       () => manager.npc_oas_category2 = true);
            CreateItem("Advanced Medal",           () => manager.npc_oas_category3 = true);

            // Time Attack
            CreateItem("Fundamentals Time Attack", () => manager.timeattack_fundamentals_progression++);
            CreateItem("Intermediate Time Attack", () => manager.timeattack_bouldering_progression++);
            CreateItem("Advanced Time Attack",     () => manager.timeattack_advanced_progression++);

#endregion

#region Alps DLC

            // Progressive unlocks for flowers
            CreateItem("Gentiana", () => {
                if (manager.alps_gentiana1 == false)      manager.alps_gentiana1 = true;
                else if (manager.alps_gentiana2 == false) manager.alps_gentiana2 = true;
                else if (manager.alps_gentiana3 == false) manager.alps_gentiana3 = true;
                else if (manager.alps_gentiana4 == false) manager.alps_gentiana4 = true;
                else if (manager.alps_gentiana5 == false) manager.alps_gentiana5 = true;
                else if (manager.alps_gentiana6 == false) manager.alps_gentiana6 = true;
                else if (manager.alps_gentiana7 == false) manager.alps_gentiana7 = true;
                else {
                    // NOTE: This should be unreachable
                }
            });
            CreateItem("Edelweiss", () => {
                if (manager.alps_edelweiss1 == false)      manager.alps_edelweiss1 = true;
                else if (manager.alps_edelweiss2 == false) manager.alps_edelweiss2 = true;
                else if (manager.alps_edelweiss3 == false) manager.alps_edelweiss3 = true;
                else if (manager.alps_edelweiss4 == false) manager.alps_edelweiss4 = true;
                else if (manager.alps_edelweiss5 == false) manager.alps_edelweiss5 = true;
                else if (manager.alps_edelweiss6 == false) manager.alps_edelweiss6 = true;
                else if (manager.alps_edelweiss7 == false) manager.alps_edelweiss7 = true;
                else {
                    // NOTE: This should be unreachable
                }
            });

            // Idols
            CreateItem("Idol of Crimps #1",          () => manager.alps_hasStatue_crimps_pt1 = true);
            CreateItem("Idol of Crimps #2",          () => manager.alps_hasStatue_crimps_pt2 = true);
            CreateItem("Idol of Cruelty #1",         () => manager.alps_hasStatue_gravity_pt1 = true);
            CreateItem("Idol of Cruelty #2",         () => manager.alps_hasStatue_gravity_pt2 = true);
            CreateItem("Idol of Feathers #1",        () => manager.alps_hasStatue_feathers_pt1 = true);
            CreateItem("Idol of Feathers #2",        () => manager.alps_hasStatue_feathers_pt2 = true);
            CreateItem("Idol of Greater Balance #1", () => manager.alps_hasStatue_greaterbalance_pt1 = true);
            CreateItem("Idol of Greater Balance #2", () => manager.alps_hasStatue_greaterbalance_pt2 = true);
            CreateItem("Idol of Ice #1",             () => manager.alps_hasStatue_ice_pt1 = true);
            CreateItem("Idol of Ice #2",             () => manager.alps_hasStatue_ice_pt2 = true);
            CreateItem("Idol of Pinches #1",         () => manager.alps_hasStatue_pinches_pt1 = true);
            CreateItem("Idol of Pinches #2",         () => manager.alps_hasStatue_pinches_pt2 = true);
            CreateItem("Idol of Pitches #1",         () => manager.alps_hasStatue_pitches_pt1 = true);
            CreateItem("Idol of Pitches #2",         () => manager.alps_hasStatue_pitches_pt2 = true);
            CreateItem("Idol of Slopers #1",         () => manager.alps_hasStatue_slopers_pt1 = true);
            CreateItem("Idol of Slopers #2",         () => manager.alps_hasStatue_slopers_pt2 = true);
            CreateItem("Idol of Sundown #1",         () => manager.alps_hasStatue_sundown_pt1 = true);
            CreateItem("Idol of Sundown #2",         () => manager.alps_hasStatue_sundown_pt2 = true);
            CreateItem("Idol of Seeds #1",           () => manager.alps_hasStatue_seeds_pt1 = true);
            CreateItem("Idol of Seeds #2",           () => manager.alps_hasStatue_seeds_pt2 = true);

#endregion

#region Extra Items

            CreateItem("Northern Range Ticket",      () => hasNorthernTicket = true);

            // Books
            CreateItem("Fundamentals Book",          () => hasFundamentalsBook = true);
            CreateItem("Intermediate Book",          () => manager.category_2_unlocked = true);
            CreateItem("Advanced Book",              () => manager.category_3_unlocked = true);
            CreateItem("Expert Book",                () => manager.category_4_unlocked = true);
            CreateItem("Essentials Book",            () => hasEssentialsBook = true);
            CreateItem("Alpine Greats Book",         () => manager.alps_category_2_unlocked = true);
            CreateItem("Arduous and Arctic Book",    () => manager.alps_category_3_unlocked = true);

            CreateAllStamps();
#endregion

        }

        /**
         * <summary>
         * Updates progression information for
         * a given peak.
         * </summary>
         * <param name="peak">The peak which was unlocked</param>
         * <param name="category">The category the peak is in</param>
         */
        private void UpdateStamp(ref bool peak, int category) {
            peak = true;

            switch (category) {
                case 0:
                    manager.category_1_progression++;
                    break;
                case 1:
                    manager.category_2_progression++;
                    break;
                case 2:
                    manager.category_3_progression++;
                    break;
                case 3:
                    manager.category_4_progression++;
                    break;
                case 4:
                    manager.alps_category1_progression++;
                    break;
                case 5:
                    manager.alps_category2_progression++;
                    break;
                case 6:
                    manager.alps_category3_progression++;
                    break;
            }

            if (category >= 0 && category <= 3) {
                manager.progression++;
            }
        }

        /**
         * <summary>
         * Creates data for all stamps.
         * </summary>
         */
        private void CreateAllStamps() {
            // Fundamentals
            CreateItem("Greenhorn's Top (Stamp)",         () => UpdateStamp(ref manager.greenhornspeak,      0));
            CreateItem("Paltry Peak (Stamp)",             () => UpdateStamp(ref manager.paltrypeak,          0));
            CreateItem("Old Mill (Stamp)",                () => UpdateStamp(ref manager.oldmill,             0));
            CreateItem("Gray Gully (Stamp)",              () => UpdateStamp(ref manager.graygully,           0));
            CreateItem("The Lighthouse (Stamp)",          () => UpdateStamp(ref manager.lighthouse,          0));
            CreateItem("Old Man of Sjór (Stamp)",         () => UpdateStamp(ref manager.oldmanofsjor,        0));
            CreateItem("Giant's Shelf (Stamp)",           () => UpdateStamp(ref manager.giantsshelf,         0));
            CreateItem("Evergreen's End (Stamp)",         () => UpdateStamp(ref manager.evergreensend,       0));
            CreateItem("The Twins (Stamp)",               () => UpdateStamp(ref manager.thetwins,            0));
            CreateItem("Old Grove's Skelf (Stamp)",       () => UpdateStamp(ref manager.oldgroveskelf,       0));
            CreateItem("Hangman's Leap (Stamp)",          () => UpdateStamp(ref manager.hangmansleap,        0));
            CreateItem("Land's End (Stamp)",              () => UpdateStamp(ref manager.landsend,            0));
            CreateItem("Old Langr (Stamp)",               () => UpdateStamp(ref manager.oldlangr,            0));
            CreateItem("Aldr Grotto (Stamp)",             () => UpdateStamp(ref manager.aldrgrotto,          0));
            CreateItem("Three Brothers (Stamp)",          () => UpdateStamp(ref manager.threebrothers,       0));
            CreateItem("Walter's Crag (Stamp)",           () => UpdateStamp(ref manager.walterscrag,         0));
            CreateItem("The Great Crevice (Stamp)",       () => UpdateStamp(ref manager.greatcrevice,        0));
            CreateItem("Old Hagger (Stamp)",              () => UpdateStamp(ref manager.oldhagger,           0));
            CreateItem("Ugsome Stórr (Stamp)",            () => UpdateStamp(ref manager.ugsomestorr,         0));
            CreateItem("Wuthering Crest (Stamp)",         () => UpdateStamp(ref manager.wutheringcrest,      0));

            // Intermediate
            CreateItem("Porter's Boulder (Stamp)",        () => UpdateStamp(ref manager.portersboulder,      1));
            CreateItem("Jotunn's Thumb (Stamp)",          () => UpdateStamp(ref manager.jotunnsthumb,        1));
            CreateItem("Old Skerry (Stamp)",              () => UpdateStamp(ref manager.oldskerry,           1));
            CreateItem("Hamarr Stone (Stamp)",            () => UpdateStamp(ref manager.hamarrstone,         1));
            CreateItem("Giant's Nose (Stamp)",            () => UpdateStamp(ref manager.giantsnose,          1));
            CreateItem("Walter's Boulder (Stamp)",        () => UpdateStamp(ref manager.waltersboulder,      1));
            CreateItem("Sundered Sons (Stamp)",           () => UpdateStamp(ref manager.sunderedsons,        1));
            CreateItem("Old Weald's Boulder (Stamp)",     () => UpdateStamp(ref manager.oldwealdsboulder,    1));
            CreateItem("Leaning Spire (Stamp)",           () => UpdateStamp(ref manager.leaningspire,        1));
            CreateItem("Cromlech (Stamp)",                () => UpdateStamp(ref manager.cromlech,            1));

            // Advanced
            CreateItem("Walker's Pillar (Stamp)",         () => UpdateStamp(ref manager.walkerspillar,       2));
            CreateItem("Great Gaol (Stamp)",              () => UpdateStamp(ref manager.greatgaol,           2));
            CreateItem("Eldenhorn (Stamp)",               () => UpdateStamp(ref manager.eldenhorn,           2));
            CreateItem("St. Haelga (Stamp)",              () => UpdateStamp(ref manager.sthaelga,            2));
            CreateItem("Ymir's Shadow (Stamp)",           () => UpdateStamp(ref manager.ymirsshadow,         2));

            // Expert
            CreateItem("Great Bulwark (Stamp)",           () => UpdateStamp(ref manager.greatbulwark,        3));
            CreateItem("Solemn Tempest (Stamp)",          () => UpdateStamp(ref manager.solemntempest,       3));

            // Essentials
            CreateItem("Tutor's Tower (Stamp)",           () => UpdateStamp(ref manager.tutortower,          4));
            CreateItem("Stougr Boulder (Stamp)",          () => UpdateStamp(ref manager.stougrboulder,       4));
            CreateItem("Mara's Arch (Stamp)",             () => UpdateStamp(ref manager.marasarch,           4));
            CreateItem("Grainne Spire (Stamp)",           () => UpdateStamp(ref manager.grainnespire,        4));
            CreateItem("Great Bók Tree (Stamp)",          () => UpdateStamp(ref manager.greatboktree,        4));
            CreateItem("Treppenwald (Stamp)",             () => UpdateStamp(ref manager.treppenwald,         4));
            CreateItem("Castle of the Swan King (Stamp)", () => UpdateStamp(ref manager.castleoftheswanking, 4));
            CreateItem("Seaside Tribune (Stamp)",         () => UpdateStamp(ref manager.seasidetribune,      4));
            CreateItem("Ivory Granites (Stamp)",          () => UpdateStamp(ref manager.ivorygranites,       4));
            CreateItem("Old Rekkja (Stamp)",              () => UpdateStamp(ref manager.oldrekkja,           4));
            CreateItem("Quietude (Stamp)",                () => UpdateStamp(ref manager.quietude,            4));
            CreateItem("Eljun's Folly (Stamp)",           () => UpdateStamp(ref manager.eljunsfolly,         4));

            // Alpine Greats
            CreateItem("Einvald Falls (Stamp)",           () => UpdateStamp(ref manager.einvaldfalls,        5));
            CreateItem("Almáttr Dam (Stamp)",             () => UpdateStamp(ref manager.almattrdam,          5));
            CreateItem("Dunderhorn (Stamp)",              () => UpdateStamp(ref manager.dunderhorn,          5));
            CreateItem("Mhòr Druim (Stamp)",              () => UpdateStamp(ref manager.mhordruim,           5));
            CreateItem("Welkin Pass (Stamp)",             () => UpdateStamp(ref manager.welkinpass,          5));

            // Arduous and Arctic
            CreateItem("Seigr Craeg (Stamp)",             () => UpdateStamp(ref manager.seigrcraeg,          6));
            CreateItem("Ullr's Chasm (Stamp)",            () => UpdateStamp(ref manager.ullrschasm,          6));
            CreateItem("Great Silf (Stamp)",              () => UpdateStamp(ref manager.greatsilf,           6));
            CreateItem("Towering Vísir (Stamp)",          () => UpdateStamp(ref manager.toweringvisir,       6));
            CreateItem("Eldris Wall (Stamp)",             () => UpdateStamp(ref manager.eldriswall,          6));
            CreateItem("Mount Mhòrgorm (Stamp)",          () => UpdateStamp(ref manager.mountmhorgorm,       6));
        }
    }
}
