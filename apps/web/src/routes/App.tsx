import { zodResolver } from "@hookform/resolvers/zod";
import { useMutation } from "@tanstack/react-query";
import { useForm } from "react-hook-form";
import { z } from "zod";

const uploadSchema = z.object({
  filename: z.string().min(1),
  contentType: z.string().min(1),
});

type UploadForm = z.infer<typeof uploadSchema>;

async function createUpload(values: UploadForm): Promise<unknown> {
  const response = await fetch("/videos/uploads", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      filename: values.filename,
      content_type: values.contentType,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to create upload");
  }

  return response.json();
}

export function App() {
  const form = useForm<UploadForm>({
    resolver: zodResolver(uploadSchema),
    defaultValues: { filename: "", contentType: "video/mp4" },
  });
  const mutation = useMutation({ mutationFn: createUpload });
  const onSubmit = form.handleSubmit((values) => {
    mutation.mutate(values);
  });

  return (
    <main className="mx-auto max-w-3xl p-8">
      <h1 className="text-3xl font-semibold">Video Transcoding Platform</h1>
      <p className="mt-2 text-slate-600">
        Create a presigned upload request, then hand the video off to backend workers.
      </p>

      <form className="mt-8 grid gap-4" onSubmit={(event) => void onSubmit(event)}>
        <label className="grid gap-1">
          <span>Filename</span>
          <input
            className="rounded border p-2"
            {...form.register("filename")}
            placeholder="sample.mp4"
          />
        </label>

        <label className="grid gap-1">
          <span>Content type</span>
          <input className="rounded border p-2" {...form.register("contentType")} />
        </label>

        <button className="rounded bg-slate-900 px-4 py-2 text-white" type="submit">
          Create upload
        </button>
      </form>
    </main>
  );
}
