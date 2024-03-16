# AI Audio Data Poisoning

AI Audio Data Poisoning is a Python script that demonstrates how to add adversarial noise to audio data. This technique, known as audio data poisoning, involves injecting imperceptible noise into audio files to manipulate the behavior of AI systems trained on this data.

## How It Works

The script adds random noise to the original audio signal, creating a "poisoned" version of the audio. This poisoned audio may still sound similar to the original to human ears but can cause misclassification or errors when processed by AI models trained on the data.

## Script Usage

### Dependencies

- `numpy`: For numerical operations and generating random noise.
- `librosa`: For loading audio files.
- `soundfile`: For saving audio files.

### Script Functions

- **add_noise**: Adds adversarial noise to the original audio signal.
- **save_poisoned_audio**: Saves the poisoned audio to a file.

### Example Usage

1. **Load the Original Audio**: Specify the path to the original audio file.
2. **Define Parameters**: Adjust the epsilon value to control the magnitude of the injected noise.
3. **Add Noise**: Execute the script to add adversarial noise to the original audio.
4. **Save Poisoned Audio**: Save the poisoned audio to a file for further analysis or experimentation.


### Disclaimer

Anthena Matrix projects are provided for educational and research purposes only. We do not take any responsibility for the misuse or unintended consequences of using our projects. Users are encouraged to use them responsibly and in compliance with applicable laws and regulations.


## License

This project is licensed under the MIT License.


## Support AnthenaMatrix

If you find our work valuable and would like to support AnthenaMatrix, you can contribute to our efforts by donating cryptocurrency:

- **Bitcoin**: `bc1qxvvtgz0vf3n2cuxt0suvf39jleegpt9wawxazn`
- **Ethereum**: `0xE73E90779B3e8F6D65306B40E02878f437408b4E`
- **BNB**: `0xE73E90779B3e8F6D65306B40E02878f437408b4E`
- **Dogecoin**: `D827LpfJu9pcVc3Kky82sTrNnsE7pLGqeV`
- **Solana**: `AJtGEJvoVoS2eeqeHQvf7usRs2nSQM1yLtBSdKp1KBY5`


## Usage Example

```python
# Define the audio path
audio_path = "original_audio.wav"

# Load the original audio file
audio, sample_rate = librosa.load(audio_path, sr=None)

# Set the epsilon value for the noise (adjust as needed)
epsilon = 0.01

# Add adversarial noise to the original audio
poisoned_audio = add_noise(audio, epsilon)

# Save the poisoned audio
save_poisoned_audio(audio_path, poisoned_audio, sample_rate)



