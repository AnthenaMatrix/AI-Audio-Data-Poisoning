import numpy as np
import librosa
import soundfile as sf

def add_noise(audio, epsilon):
    # Generate random noise with the same length as the audio
    noise = np.random.uniform(low=-epsilon, high=epsilon, size=len(audio))

    # Add noise to the audio signal
    noisy_audio = audio + noise

    return noisy_audio

def save_poisoned_audio(audio_path, poisoned_audio, sample_rate):
    # Save the poisoned audio to a file
    sf.write("poisoned_" + audio_path, poisoned_audio, sample_rate)
    print("Poisoned audio saved successfully.")

# Example usage:
if __name__ == "__main__":
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
