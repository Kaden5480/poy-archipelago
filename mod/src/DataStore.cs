using PoYArchipelago.Data;

namespace PoYArchipelago {
    public class DataStore {
        // Data for all items
        public Items items { get; }

        /**
         * <summary>
         * Initializes the data store.
         * </summary>
         */
        public DataStore() {
            IDHandler handler = new IDHandler();

            this.items = new Items(handler);
        }
    }
}
