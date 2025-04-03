using System;

namespace PoYArchipelago.Data {
    /**
     * <summary>
     * Data for an item.
     * </summary>
     */
    public class ItemData {
        public long id { get; }
        public string name { get; }

        private Action unlockMethod { get; }

        /**
         * <summary>
         * Creates a new ItemData object.
         *
         * NOTE: After each unlock, GameManager.control.Save() is called.
         * </summary>
         * <param name="id">The ID of this object</param>
         * <param name="name">The name of this object</param>
         * <param name="unlockMethod">The method to execute to unlock this item</param>
         */
        public ItemData(
            long id,
            string name,
            Action unlockMethod
        ) {
            this.id = id;
            this.name = name;
            this.unlockMethod = unlockMethod;
        }

        /**
         * <summary>
         * Unlocks this item, giving the player some item
         * in game.
         *
         * NOTE: This also calls GameManager.control.Save().
         * </summary>
         */
        public void Unlock() {
            unlockMethod();
            GameManager.control.Save();
        }
    }
}
