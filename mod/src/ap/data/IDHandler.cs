namespace PoYArchipelago.AP.Data {
    public class IDHandler {
        // The default ID
        private long id = 1;

        /**
         * <summary>
         * Gets a new ID for assigning to data.
         * </summary>
         * <returns>The new ID</returns>
         */
        public long NewID() {
            long new_id = id;
            id++;

            return id;
        }
    }
}
