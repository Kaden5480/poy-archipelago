using UnityEngine;

namespace PoYArchipelago.Patches {
    public class LocationManager : GameManager {
        public static LocationManager instance { get; private set; } = null;

        public static void Create() {
            if (instance != null) {
                return;
            }

            GameObject obj = new GameObject("PoYArchipelago Location Manager");
            GameObject.DontDestroyOnLoad(obj);
            instance = obj.AddComponent<LocationManager>();
        }

        public void Awake() {}

        private void _Load() {
            base.Load();
        }

        private void _Save() {
            base.Save();
        }

        public static void LoadData() {
            instance._Load();
        }

        public static void SaveData() {
            instance._Save();
        }
    }
}
